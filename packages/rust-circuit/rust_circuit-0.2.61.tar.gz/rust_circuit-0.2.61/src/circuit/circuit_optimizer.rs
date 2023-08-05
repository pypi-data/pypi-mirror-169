use crate::{all_imports::Shape, circuit::repr::RustRepr, hashmaps::FxHashMap as HashMap};

use num_bigint::BigUint;

use crate::{circuit::print::rust_expression_notation_circuit, pyo3_prelude::*};

use super::{
    canonicalize::deep_canonicalize,
    compiler_heuristics::deep_maybe_distribute,
    compiler_strip::strip_names,
    debugging::{create_circuit_test, randn_ablate_great_grandchildren},
    deep_rewrite::deep_heuristic_nest_adds,
    deep_rewrite::{compiler_simp, deep_optimize_einsums, deep_push_down_index},
    flat_concat, get_compatible_dtype,
    scheduled_execution::{
        circuit_to_schedule, circuit_to_schedule_naive_toposort, Schedule, SchedulingError,
    },
    CircuitNode, CircuitRc, HashBytes,
};
use crate::opt_einsum::EinsumSpec;
use crate::{py_types::Tensor, timed, util::apply_fn_until_same};

// a lot of the function boundries in this are there because it would be too hard to optimize things jointly
// not because we don't need to optimize things jointly
// like scheduling does impact whether you should distribute, but using that info would be
// difficult

#[pyclass]
#[derive(Debug, Clone, Copy, PyClassDeriv)]
pub struct OptimizationSettings {
    #[pyo3(get, set)]
    pub verbose: usize,
    #[pyo3(get, set)]
    pub max_memory: usize,
    #[pyo3(get, set)]
    pub max_single_tensor_memory: usize,
    #[pyo3(get, set)]
    pub max_memory_fallback: Option<usize>,
    #[pyo3(get, set)]
    pub scheduling_num_mem_chunks: usize,
    #[pyo3(get, set)]
    pub distribute_min_size: Option<usize>,
    #[pyo3(get, set)]
    pub scheduling_naive: bool,
    #[pyo3(get, set)]
    pub scheduling_simplify: bool,
    #[pyo3(get, set)]
    pub scheduling_timeout: usize,
    #[pyo3(get, set)]
    pub scheduling_simplify_lossy: bool,
    #[pyo3(get, set)]
    pub adjust_numerical_scale: bool,
    #[pyo3(get, set)]
    pub numerical_scale_min: f64,
    #[pyo3(get, set)]
    pub numerical_scale_max: f64,
    #[pyo3(get, set)]
    pub capture_and_print: bool,
    #[pyo3(get, set)]
    pub create_tests: bool,
    #[pyo3(get, set)]
    pub log_simplifications: bool,
    #[pyo3(get, set)]
    pub log_slow_einsums: bool,
}

#[cfg(not(feature = "real-pyo3"))]
impl<'source> FromPyObject<'source> for OptimizationSettings {
    fn extract(_: &'source PyAny) -> PyResult<Self> {
        unimplemented!()
    }
}

impl Default for OptimizationSettings {
    fn default() -> Self {
        Self {
            verbose: 0,
            max_memory: 9_000_000_000,
            max_single_tensor_memory: 9_000_000_000,
            max_memory_fallback: None,
            scheduling_num_mem_chunks: 200,
            distribute_min_size: None,
            scheduling_naive: false,
            scheduling_timeout: 5_000,
            scheduling_simplify: false,
            scheduling_simplify_lossy: false,
            adjust_numerical_scale: false,
            numerical_scale_min: 1e-8,
            numerical_scale_max: 1e8,
            capture_and_print: false,
            create_tests: false,
            log_simplifications: false,
            log_slow_einsums: false,
        }
    }
}

#[pymethods]
impl OptimizationSettings {
    #[new]
    #[args(
        verbose = "OptimizationSettings::default().verbose",
        max_memory = "OptimizationSettings::default().max_memory",
        max_single_tensor_memory = "OptimizationSettings::default().max_single_tensor_memory",
        max_memory_fallback = "None",
        scheduling_num_mem_chunks = "OptimizationSettings::default().scheduling_num_mem_chunks",
        distribute_min_size = "None",
        scheduling_naive = "OptimizationSettings::default().scheduling_naive",
        scheduling_timeout = "OptimizationSettings::default().scheduling_timeout",
        scheduling_simplify = "OptimizationSettings::default().scheduling_simplify",
        scheduling_simplify_lossy = "OptimizationSettings::default().scheduling_simplify_lossy",
        adjust_numerical_scale = "OptimizationSettings::default().adjust_numerical_scale",
        numerical_scale_min = "OptimizationSettings::default().numerical_scale_min",
        numerical_scale_max = "OptimizationSettings::default().numerical_scale_max",
        capture_and_print = "OptimizationSettings::default().capture_and_print",
        create_tests = "OptimizationSettings::default().create_tests",
        log_simplifications = "OptimizationSettings::default().log_simplifications",
        log_slow_einsums = "OptimizationSettings::default().log_slow_einsums"
    )]
    fn new(
        verbose: usize,
        max_memory: usize,
        max_single_tensor_memory: usize,
        max_memory_fallback: Option<usize>,
        scheduling_num_mem_chunks: usize,
        distribute_min_size: Option<usize>,
        scheduling_naive: bool,
        scheduling_timeout: usize,
        scheduling_simplify: bool,
        scheduling_simplify_lossy: bool,
        adjust_numerical_scale: bool,
        numerical_scale_min: f64,
        numerical_scale_max: f64,
        capture_and_print: bool,
        create_tests: bool,
        log_simplifications: bool,
        log_slow_einsums: bool,
    ) -> Self {
        Self {
            verbose,
            max_memory,
            max_single_tensor_memory,
            max_memory_fallback,
            scheduling_num_mem_chunks,
            distribute_min_size,
            scheduling_naive,
            scheduling_timeout,
            scheduling_simplify,
            scheduling_simplify_lossy,
            adjust_numerical_scale,
            numerical_scale_min,
            numerical_scale_max,
            capture_and_print,
            create_tests,
            log_simplifications,
            log_slow_einsums,
        }
    }
}

#[derive(Debug, Clone, Default)]
pub struct OptimizationCache {
    pub simplified: HashMap<HashBytes, CircuitRc>,
    pub distributed: HashMap<HashBytes, Option<CircuitRc>>,
    pub flops: HashMap<HashBytes, BigUint>,
    pub sum_of_node_sizes: HashMap<HashBytes, BigUint>,
    pub canonicalized: HashMap<HashBytes, Option<CircuitRc>>,
    pub times_distributed: usize,
    pub simplification_log: Vec<&'static str>,
    pub max_tensor_elements: usize,
    pub max_single_tensor_numel: usize,
    pub fallback_total_numel: usize,
    pub slow_einsum_log: Vec<EinsumSpec>,
}

#[derive(Debug, Clone, Default)]
pub struct OptimizationContext {
    pub cache: OptimizationCache,
    pub settings: OptimizationSettings,
}
impl OptimizationContext {
    pub fn new_settings(settings: OptimizationSettings) -> Self {
        Self {
            cache: Default::default(),
            settings,
        }
    }
    pub fn new_settings_circuit(settings: OptimizationSettings, circuit: CircuitRc) -> Self {
        let mut result = Self {
            cache: Default::default(),
            settings,
        };
        let dtype = get_compatible_dtype(&circuit);
        result.cache.max_tensor_elements = settings.max_memory / dtype.size();
        result.cache.max_single_tensor_numel = settings.max_single_tensor_memory / dtype.size();
        result.cache.fallback_total_numel =
            settings.max_memory_fallback.unwrap_or(settings.max_memory) / dtype.size();
        result
    }

    pub fn stringify_logs(&self) -> String {
        format!(
            "let slow_einsums = {}; let simplifications= {};",
            self.cache.slow_einsum_log.repr(),
            self.cache.simplification_log.repr()
        )
    }
}

#[pyfunction]
#[pyo3(name = "optimize_circuit")]
pub fn optimize_circuit_py(circuit: CircuitRc, settings: OptimizationSettings) -> CircuitRc {
    let mut context = OptimizationContext {
        settings,
        ..Default::default()
    };
    optimize_circuit(circuit, &mut context)
}

pub fn optimize_circuit(circuit: CircuitRc, context: &mut OptimizationContext) -> CircuitRc {
    let print_timings = context.settings.verbose >= 2;
    let circuit = timed!(strip_names(circuit), 10, print_timings);
    let circuit = timed!(deep_canonicalize(circuit, context), 10, print_timings);
    if context.settings.verbose >= 4 {
        println!("Original Circuit");
        circuit.compiler_print();
    }
    if context.settings.create_tests {
        // Make compiler_simp tests here
        let ablated = randn_ablate_great_grandchildren(circuit.clone());
        create_circuit_test(
            "compiler_simp",
            ablated.clone(),
            compiler_simp(&ablated, context),
        )
        .unwrap();
    }
    let circuit = timed!(compiler_simp(&circuit, context), 10, print_timings);
    // originally tried push_down_index in compiler_simp, but that produced worse circuits
    // for unknown reasons, maybe i'll investigate
    let circuit = timed!(deep_push_down_index(circuit, None), 10, print_timings);
    let circuit = timed!(compiler_simp(&circuit, context), 10, print_timings);
    let circuit = timed!(deep_canonicalize(circuit, context), 10, print_timings);
    if context.settings.verbose >= 3 {
        println!("Simplified Circuit");
        circuit.compiler_print();
    }
    let circuit = timed!(
        apply_fn_until_same(&circuit, |x| {
            let distributed = deep_maybe_distribute(x, context);
            compiler_simp(&distributed, context)
        }),
        10,
        print_timings
    );

    let circuit = timed!(deep_canonicalize(circuit, context), 10, print_timings);
    if context.settings.verbose >= 2 {
        println!("Distributed Circuit");
        circuit.compiler_print();
    }
    let circuit = timed!(deep_heuristic_nest_adds(circuit), 10, print_timings);
    let circuit = timed!(deep_canonicalize(circuit, context), 10, print_timings);

    let circuit = timed!(deep_optimize_einsums(circuit, context), 10, print_timings);

    let circuit = timed!(deep_canonicalize(circuit, context), 10, print_timings);
    if context.settings.verbose >= 3 {
        println!("Final Circuit");
        circuit.compiler_print();
    }
    circuit
}

#[pyfunction]
pub fn optimize_to_schedule(
    circuit: CircuitRc,
    settings: OptimizationSettings,
) -> Result<Schedule, SchedulingError> {
    let mut context = &mut OptimizationContext::new_settings_circuit(settings, circuit.clone());
    let verbose = settings.verbose;
    if verbose > 0 {
        println!("Optimizing verbose {}", verbose)
    }
    if settings.capture_and_print {
        println!(
            "{}",
            rust_expression_notation_circuit(circuit.clone(), true)
        );
    }
    let optimized_circuit = timed!(optimize_circuit(circuit, &mut context), 10, verbose >= 1);
    // return evaluate_fn(&*optimized_circuit).unwrap();
    let schedule = if settings.scheduling_naive {
        circuit_to_schedule_naive_toposort(optimized_circuit)
    } else {
        timed!(
            circuit_to_schedule(optimized_circuit, context),
            10,
            verbose >= 1
        )?
    };
    if verbose > 1 {
        println!("{}", schedule.get_stats());
    }
    Ok(schedule)
}

#[pyfunction]
pub fn optimize_and_evaluate(
    circuit: CircuitRc,
    settings: OptimizationSettings,
) -> Result<Tensor, SchedulingError> {
    let schedule = optimize_to_schedule(circuit, settings)?;

    Ok(schedule.evaluate(settings))
}

/// in python, lots of functions take in collections of circuits and operate on them at once
/// with node caching for just that batch
/// because functions that take one circuit already cache nodes, it's convenient to compute multiple nodes
/// by flat-concatting and then passing around as one circuit
/// flat concatting then splitting is an extra copy on all return data,
/// which we could get rid of by removing flat-concat after rewrites (which would only work with a black box flat_concat node bc simplification isn't guaranteed to preserve concat at at end)
#[pyfunction]
pub fn optimize_and_evaluate_many(
    circuits: Vec<CircuitRc>,
    settings: OptimizationSettings,
) -> Result<Vec<Tensor>, SchedulingError> {
    let schedule = optimize_to_schedule_many(circuits, settings)?;
    Ok(schedule.evaluate_many(settings))
}

#[pyfunction]
pub fn optimize_to_schedule_many(
    circuits: Vec<CircuitRc>,
    settings: OptimizationSettings,
) -> Result<Schedule, SchedulingError> {
    let flat_concatted = flat_concat(circuits.clone()).rc();
    let mut schedule = optimize_to_schedule(flat_concatted, settings)?;
    schedule.split_shapes = Some(
        circuits
            .iter()
            .map(|x| x.info().shape.clone())
            .collect::<Vec<Shape>>(),
    );
    Ok(schedule)
}

use crate::all_imports::{TensorAxisIndex, TensorIndex};
use crate::circuit::deep_map_fallible_pre_new_children;
use crate::hashmaps::FxHashMap as HashMap;
use crate::lazy::GILLazyPy;
use crate::{pycall, pyo3_prelude::*, sv};
use std::iter::zip;

use super::{
    deep_map_op_pre_new_children, deep_map_unwrap_preorder, prelude::*, Add, CachedCircuitInfo,
    CircResult, Concat, GeneralFunction, HashBytes, Index, Rearrange, Scatter,
};
use crate::py_types::PY_UTILS;
use crate::{
    circuit::{ArrayConstant, Einsum, PyCircuitBase, Symbol},
    circuit_node_auto_impl, circuit_node_extra_impl, new_rc_unwrap,
    py_types::py_address,
    tensor_util::{Shape, TorchDeviceDtype},
};

use macro_rules_attribute::apply;
use pyo3::types::PyDict;
use pyo3::types::PyTuple;
use uuid::uuid;

#[pyfunction]
#[pyo3(name = "expand_node")]
pub fn expand_node_py(circuit: CircuitRc, inputs: Vec<CircuitRc>) -> CircResult {
    expand_node(&circuit, &inputs)
}

pub fn expand_node(circuit: &Circuit, inputs: &Vec<CircuitRc>) -> CircResult {
    if inputs.len() != circuit.children().count() {
        return Err(CircuitConstructionError::ModuleNodeWrongNumberChildren {
            expected: circuit.children().count(),
            got: inputs.len(),
        });
    }
    let batch_ranks: Vec<usize> = zip(circuit.children(), inputs)
        .filter_map(|(old, new)| new.info().rank().checked_sub(old.info().rank()))
        .collect();
    if batch_ranks.len() != inputs.len() {
        return Err(CircuitConstructionError::BatchingRankTooLow {
            default: circuit.children().map(|x| x.info().rank()).collect(),
            got: inputs.iter().map(|x| x.info().rank()).collect(),
        });
    }
    let batch_shapes: Vec<&[usize]> = zip(&batch_ranks, inputs)
        .map(|(br, new)| &new.info().shape[0..*br])
        .collect();
    match circuit {
        Circuit::Symbol(_) | Circuit::ScalarConstant(_) => Ok(circuit.clone().rc()),
        Circuit::Rearrange(node) => {
            let input_shape_non_batch = inputs[0].info().shape[batch_ranks[0]..]
                .iter()
                .cloned()
                .collect();
            let mut new_spec = node
                .spec
                .conform_to_input_shape(&input_shape_non_batch, false)
                .map_err(|e| CircuitConstructionError::RearrangeWrongInputShape {
                    spec: node.spec.clone(),
                    shape: input_shape_non_batch.clone(),
                })?
                .add_batch_dims(batch_ranks[0]);
            Ok(Rearrange::nrc(
                inputs[0].clone(),
                new_spec,
                circuit.name_cloned(),
            ))
        }
        Circuit::Index(node) => {
            // for now non-batch non-identity dims can't change
            for i in 0..node.node.info().rank() {
                if node.node.info().shape[i] != inputs[0].info().shape[i + batch_ranks[0]]
                    && node.index.0[i] != TensorAxisIndex::IDENT
                {
                    return Err(CircuitConstructionError::ExpandingFixedIndex {
                        index: node.index.clone(),
                        old_shape: node.node.info().shape.clone(),
                        new_shape: inputs[0].info().shape.clone(),
                    });
                }
            }
            Ok(Index::nrc(
                inputs[0].clone(),
                TensorIndex(
                    vec![TensorAxisIndex::IDENT; batch_ranks[0]]
                        .into_iter()
                        .chain(node.index.0.iter().cloned())
                        .collect(),
                ),
                node.name_cloned(),
            ))
        }
        Circuit::Scatter(node) => {
            // for now non-batch non-identity dims can't change
            if node.node.info().shape[..] != inputs[0].info().shape[batch_ranks[0]..] {
                return Err(CircuitConstructionError::ExpandingFixedIndex {
                    index: node.index.clone(),
                    old_shape: node.node.info().shape.clone(),
                    new_shape: inputs[0].info().shape.clone(),
                });
            }
            Ok(Scatter::nrc(
                inputs[0].clone(),
                TensorIndex(
                    vec![TensorAxisIndex::IDENT; batch_ranks[0]]
                        .into_iter()
                        .chain(node.index.0.iter().cloned())
                        .collect(),
                ),
                inputs[0].info().shape[0..batch_ranks[0]]
                    .iter()
                    .cloned()
                    .chain(node.info().shape.iter().cloned())
                    .collect(),
                node.name_cloned(),
            ))
        }
        Circuit::Concat(node) => {
            if !batch_shapes.iter().all(|x| x == &batch_shapes[0]) {
                return Err(CircuitConstructionError::InconsistentBatches {
                    batch_shapes: batch_shapes
                        .iter()
                        .map(|x| x.iter().cloned().collect())
                        .collect(),
                });
            }
            if !zip(&node.nodes, zip(inputs, &batch_ranks)).all(|(old, (new, br))| {
                old.info().shape[node.axis] == new.info().shape[node.axis + br]
            }) {
                return Err(CircuitConstructionError::ExpandingConcatAxis {
                    axis: node.axis,
                    old_shape: sv![],
                    new_shape: sv![],
                });
            }
            Concat::try_new(
                inputs.clone(),
                node.axis + batch_ranks[0],
                node.name_cloned(),
            )
            .map(|x| x.rc())
        }
        Circuit::Add(node) => Add::try_new(inputs.clone(), node.name_cloned()).map(|x| x.rc()),
        Circuit::GeneralFunction(node) => {
            GeneralFunction::try_new(inputs.clone(), node.spec.clone(), node.name_cloned())
                .map(|x| x.rc())
        }
        Circuit::Einsum(node) => {
            let mut batch_shape: Option<&[usize]> = None;
            for bs in &batch_shapes {
                if !bs.is_empty() {
                    if let Some(existing) = batch_shape {
                        if *bs != &existing[..] {
                            return Err(CircuitConstructionError::InconsistentBatches {
                                batch_shapes: batch_shapes
                                    .iter()
                                    .map(|x| x.iter().cloned().collect())
                                    .collect(),
                            });
                        }
                    } else {
                        batch_shape = Some(bs.clone());
                    }
                }
            }
            let next_axis = node.next_axis();
            let newies = || (next_axis as u8..next_axis + batch_shape.unwrap().len() as u8);
            let out_axes = if let Some(bs) = batch_shape {
                newies().chain(node.out_axes.iter().cloned()).collect()
            } else {
                node.out_axes.clone()
            };
            Einsum::try_new(
                node.args
                    .iter()
                    .enumerate()
                    .map(|(i, (child, ints))| {
                        (inputs[i].clone(), {
                            if !batch_shapes[i].is_empty() {
                                newies().chain(ints.iter().cloned()).collect()
                            } else {
                                ints.clone()
                            }
                        })
                    })
                    .collect(),
                out_axes,
                node.name_cloned(),
            )
            .map(|x| x.rc())
        }
        _ => Err(CircuitConstructionError::UnknownGeneralFunction {
            spec_name: "hi".to_owned(),
        }),
    }
}

#[pyfunction]
#[pyo3(name = "replace_expand_bottom_up_dict")]
pub fn replace_expand_bottom_up_dict_py(
    circuit: CircuitRc,
    dict: HashMap<CircuitRc, CircuitRc>,
) -> CircResult {
    replace_expand_bottom_up(circuit, |x| dict.get(&x.clone().rc()).cloned())
}

#[pyfunction]
#[pyo3(name = "replace_expand_bottom_up")]
pub fn replace_expand_bottom_up_py(circuit: CircuitRc, f: PyObject) -> CircResult {
    replace_expand_bottom_up(circuit, |x| pycall!(f, (x.clone().rc(),)))
}

pub fn replace_expand_bottom_up<F>(
    circuit: CircuitRc,
    replacer: F,
) -> Result<CircuitRc, CircuitConstructionError>
where
    F: Fn(&Circuit) -> Option<CircuitRc>,
{
    let recursor = |circuit: &Circuit,
                    new_children: &Vec<CircuitRc>|
     -> Result<CircuitRc, CircuitConstructionError> {
        if let Some(replaced) = replacer(&circuit) {
            return Ok(replaced);
        }
        expand_node(circuit, new_children)
    };
    deep_map_fallible_pre_new_children(&**circuit, recursor)
}

#[pyclass(unsendable)]
#[derive(Debug, Clone, PyClassDeriv, Hash, PartialEq, Eq)]
pub struct ModuleNodeSpec {
    #[pyo3(get)]
    pub spec_circuit: CircuitRc,
    #[pyo3(get)]
    pub input_specs: Vec<ModuleNodeArgSpec>,
    #[pyo3(get)]
    pub name: Option<String>,
}

impl ModuleNodeSpec {
    pub fn expand(&self, nodes: &Vec<CircuitRc>) -> CircResult {
        if self.input_specs.len() != nodes.len() {
            return Err(CircuitConstructionError::ModuleNodeWrongNumberChildren {
                expected: self.input_specs.len(),
                got: nodes.len(),
            });
        }
        for (spec, node) in zip(self.input_specs.iter(), nodes) {
            if node.info().rank() < spec.symbol.info().rank() {
                // todo error messages
                return Err(CircuitConstructionError::InconsistentBatches {
                    batch_shapes: vec![],
                });
            }
            if !spec.batchable && node.info().rank() > spec.symbol.info().rank() {
                return Err(CircuitConstructionError::InconsistentBatches {
                    batch_shapes: vec![],
                });
            }
            if !spec.expandable
                && node.info().shape[node.info().rank() - spec.symbol.info().rank()..]
                    != spec.symbol.info().shape[..]
            {
                return Err(CircuitConstructionError::InconsistentBatches {
                    batch_shapes: vec![],
                });
            }
        }
        replace_expand_bottom_up(self.spec_circuit.clone(), |c| {
            if let Some(i) = self
                .input_specs
                .iter()
                .position(|x| &x.symbol.clone().c() == c)
            {
                Some(nodes[i].clone())
            } else {
                None
            }
        })
    }

    pub fn compute_hash(&self) -> HashBytes {
        let mut hasher = blake3::Hasher::new();
        hasher.update(&self.spec_circuit.info().hash);
        for input_spec in &self.input_specs {
            hasher.update(&[input_spec.batchable as u8, input_spec.expandable as u8]);
            hasher.update(&input_spec.symbol.info().hash);
        }
        hasher.finalize().into()
    }
}
#[pymethods]
impl ModuleNodeSpec {
    #[new]
    fn new(
        spec_circuit: CircuitRc,
        input_specs: Vec<ModuleNodeArgSpec>,
        name: Option<String>,
    ) -> Self {
        Self {
            spec_circuit,
            input_specs,
            name,
        }
    }
}

#[pyclass(unsendable)]
#[derive(Debug, Clone, PyClassDeriv, Hash, PartialEq, Eq)]
pub struct ModuleNodeArgSpec {
    #[pyo3(get)]
    pub symbol: Symbol,
    #[pyo3(get)]
    pub batchable: bool,
    #[pyo3(get)]
    pub expandable: bool,
}
#[pymethods]
impl ModuleNodeArgSpec {
    #[new]
    fn new(symbol: Symbol, batchable: bool, expandable: bool) -> Self {
        Self {
            symbol,
            batchable,
            expandable,
        }
    }
}

#[pyclass(unsendable, extends=PyCircuitBase)]
#[derive(Debug, Clone, PyClassDeriv)]
pub struct ModuleNode {
    #[pyo3(get)]
    pub nodes: Vec<CircuitRc>,
    #[pyo3(get)]
    pub spec: ModuleNodeSpec,
    #[pyo3(get)]
    pub cached_full_circuit: CircuitRc,
    info: CachedCircuitInfo,
    #[pyo3(get)]
    name: Option<String>,
}

impl ModuleNode {
    #[apply(new_rc_unwrap)]
    pub fn try_new(
        nodes: Vec<CircuitRc>,
        spec: ModuleNodeSpec,
        name: Option<String>,
    ) -> (Result<Self, CircuitConstructionError>) {
        let cached_full_circuit = spec.expand(&nodes).map_err(|e| {
            CircuitConstructionError::ModuleNodeExpansionError { error: Box::new(e) }
        })?;
        let mut out = Self {
            nodes,
            spec,
            cached_full_circuit,
            name: name.clone(),
            info: Default::default(),
        };
        out.name = out.auto_name(name);
        out.init_info()
    }

    pub fn new_kwargs(
        kwargs: &HashMap<String, CircuitRc>,
        spec: ModuleNodeSpec,
        name: Option<String>,
    ) -> Result<Self, CircuitConstructionError> {
        let mut nodes: Vec<CircuitRc> = vec![spec.spec_circuit.clone(); spec.input_specs.len()];
        for (k, v) in kwargs {
            match spec
                .input_specs
                .iter()
                .position(|x| x.symbol.name().map(|n| n == k).unwrap_or(false))
            {
                Some(i) => {
                    nodes[i] = v.clone();
                }
                None => {
                    return Err(CircuitConstructionError::ModuleNodeUnknownArgument {
                        argument: k.clone(),
                    })
                }
            }
        }
        Self::try_new(nodes, spec, name)
    }
}

circuit_node_extra_impl!(ModuleNode);

impl CircuitNode for ModuleNode {
    circuit_node_auto_impl!("6825f723-f178-4dab-b568-cd85eb6d2bf3");

    fn compute_shape(&self) -> Shape {
        self.cached_full_circuit.info().shape.clone()
    }

    fn compute_hash(&self) -> blake3::Hasher {
        let mut hasher = blake3::Hasher::new();
        for node in &self.nodes {
            hasher.update(&node.info().hash);
        }
        hasher.update(uuid!("8995f508-a7a5-4025-8d10-e46f55825cd1").as_bytes());
        hasher.update(&self.spec.compute_hash());
        hasher
    }

    fn children<'a>(&'a self) -> Box<dyn Iterator<Item = CircuitRc> + 'a> {
        Box::new(self.nodes.iter().cloned())
    }

    fn map_children_enumerate<'a, F, E>(
        &'a self,
        mut f: F,
    ) -> Result<Self, CircuitConstructionError>
    where
        CircuitConstructionError: From<E>,
        F: FnMut(usize, &'a Circuit) -> Result<CircuitRc, E>,
    {
        Self::try_new(
            self.nodes
                .iter()
                .enumerate()
                .map(move |(i, circ)| f(i, circ))
                .collect::<Result<Vec<_>, _>>()?,
            self.spec.clone(),
            self.name.clone(),
        )
    }

    fn child_axis_map(&self) -> Vec<Vec<Option<usize>>> {
        vec![] // todo: return child axis map
    }

    fn eval_tensors(
        &self,
        tensors: &[crate::py_types::Tensor],
        _device_dtype: &TorchDeviceDtype,
    ) -> Result<crate::py_types::Tensor, super::TensorEvalError> {
        unimplemented!();
    }
}

impl CircuitNodeAutoName for ModuleNode {
    fn auto_name(&self, name: Option<String>) -> Option<String> {
        name.or_else(|| {
            if self.children().all(|x| x.name().is_none()) || self.spec.name.is_none() {
                None
            } else {
                Some(
                    self.spec.name.clone().unwrap()
                        + " "
                        + &self
                            .children()
                            .filter_map(|x| x.name().map(|y| y.to_owned()))
                            .collect::<Vec<String>>()
                            .join(" , "),
                )
            }
        })
    }
}

#[pymethods]
impl ModuleNode {
    #[cfg(feature = "real-pyo3")]
    #[new]
    #[args(spec, name, py_kwargs = "**")]
    fn new(
        spec: ModuleNodeSpec,
        name: Option<String>,
        py_kwargs: Option<&PyDict>,
    ) -> PyResult<PyClassInitializer<ModuleNode>> {
        let dict: HashMap<String, CircuitRc> = py_kwargs.unwrap().extract().unwrap();
        Ok(ModuleNode::new_kwargs(&dict, spec, name)?.into_init())
    }

    #[staticmethod]
    fn new_flat(
        nodes: Vec<CircuitRc>,
        spec: ModuleNodeSpec,
        name: Option<String>,
    ) -> (Result<Self, CircuitConstructionError>) {
        Self::try_new(nodes, spec, name)
    }
}

#[pyfunction]
pub fn inline_all_modules(circuit: CircuitRc) -> CircuitRc {
    deep_map_unwrap_preorder(&circuit, |c| match c {
        Circuit::ModuleNode(mn) => mn.cached_full_circuit.clone(),
        _ => c.clone().rc(),
    })
}

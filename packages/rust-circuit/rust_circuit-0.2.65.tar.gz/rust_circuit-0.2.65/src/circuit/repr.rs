use smallvec::Array;
use uuid::Uuid;

use super::{OpSize, RearrangeSpec, TensorAxisIndex, TensorIndex};
use crate::{
    all_imports::TorchDeviceDtypeOp, opt_einsum::EinsumSpec, rrfs::save_tensor_rrfs, smallvec::Sv,
    tensor_util::Shape,
};

pub trait RustRepr {
    /// Serialize objects to Rust expression source code
    fn repr(&self) -> String;
}

impl RustRepr for u8 {
    fn repr(&self) -> String {
        format!("{}", self)
    }
}
impl RustRepr for usize {
    fn repr(&self) -> String {
        format!("{}", self)
    }
}
impl RustRepr for i64 {
    fn repr(&self) -> String {
        format!("{}", self)
    }
}
impl RustRepr for f64 {
    fn repr(&self) -> String {
        format!("{}_f64", self)
    }
}
impl RustRepr for OpSize {
    fn repr(&self) -> String {
        format!("OpSize::from({})", Option::<usize>::from(*self).repr())
    }
}
impl RustRepr for String {
    fn repr(&self) -> String {
        format!("\"{}\".to_owned()", self)
    }
}
impl RustRepr for &str {
    fn repr(&self) -> String {
        format!("\"{}\"", self)
    }
}
impl RustRepr for Uuid {
    fn repr(&self) -> String {
        format!("uuid!(\"{}\")", self)
    }
}

impl<T: RustRepr> RustRepr for Option<T> {
    fn repr(&self) -> String {
        match self {
            Some(x) => format!("Some({})", x.repr()),
            None => "None".to_owned(),
        }
    }
}

impl<T: RustRepr> RustRepr for Vec<T> {
    fn repr(&self) -> String {
        let strings: Vec<String> = self.iter().map(|s| s.repr()).collect();
        format!("vec![{}]", strings.join(","))
    }
}

impl<T: Array> RustRepr for Sv<T>
where
    T::Item: RustRepr,
{
    fn repr(&self) -> String {
        let strings: Vec<String> = self.iter().map(|s| s.repr()).collect();
        format!("sv![{}]", strings.join(","))
    }
}

impl RustRepr for RearrangeSpec {
    fn repr(&self) -> String {
        format!(
            "RearrangeSpec::new({}, {}, {})",
            self.input_ints.repr(),
            self.output_ints.repr(),
            self.int_sizes.repr()
        )
    }
}

impl RustRepr for EinsumSpec {
    fn repr(&self) -> String {
        format!(
            "EinsumSpec{{input_ints:{}, output_ints:{}, int_sizes:{}}}",
            self.input_ints.repr(),
            self.output_ints.repr(),
            self.int_sizes.repr()
        )
    }
}

impl RustRepr for TorchDeviceDtypeOp {
    fn repr(&self) -> String {
        if let (None, None) = (&self.device, &self.dtype) {
            "TorchDeviceDtypeOp::default()".to_owned()
        } else {
            format!(
                "TorchDeviceDtypeOp {{ device: {}, dtype: {} }}",
                self.device.repr(),
                self.dtype.repr(),
            )
        }
    }
}

pub struct ReprWrapper(pub String);

impl RustRepr for ReprWrapper {
    fn repr(&self) -> String {
        self.0.clone()
    }
}

impl TensorAxisIndex {
    pub fn repr(
        &self,
        bound: usize,
        device_dtype: &TorchDeviceDtypeOp,
        tensors_as_randn: bool,
    ) -> String {
        match self {
            TensorAxisIndex::Single(i) => format!("TensorAxisIndex::Single({})", i),
            TensorAxisIndex::Tensor(t) => {
                if tensors_as_randn {
                    format!(
                        "TensorAxisIndex::new_tensor_randint_seeded({}, {}, {}, {})",
                        t.shape()[0].repr(),
                        bound.repr(),
                        device_dtype.repr(),
                        t.hash_usize().unwrap(),
                    )
                } else {
                    let hash_base16: &str = &save_tensor_rrfs(t.clone()).unwrap();
                    format!(
                        "TensorAxisIndex::Tensor(tensor_from_hash({}).unwrap())",
                        hash_base16.repr()
                    )
                }
            }
            TensorAxisIndex::Slice(s) => format!(
                "TensorAxisIndex::Slice(Slice {{ start:{}, stop:{} }})",
                s.start.repr(),
                s.stop.repr()
            ),
        }
    }
}

impl TensorIndex {
    pub fn repr(
        &self,
        shape: Shape,
        device_dtype: &TorchDeviceDtypeOp,
        tensors_as_randn: bool,
    ) -> String {
        // shape: shape of the tensor we're indexing into
        format!(
            "TensorIndex ( vec![{}] )",
            self.0
                .iter()
                .enumerate()
                .map(|(i, tensor_axis_index)| tensor_axis_index.repr(
                    shape[i],
                    device_dtype,
                    tensors_as_randn
                ))
                .collect::<Vec<String>>()
                .join(", ")
        )
    }
}

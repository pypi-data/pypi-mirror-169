use crate::pyo3_prelude::*;
use crate::{
    circuit::ArrayConstant,
    py_types::{Tensor, PY_UTILS},
};
use base16::encode_lower;

pub fn get_rrfs_dir() -> String {
    std::env::var("RRFS_DIR").unwrap_or_else(|_e| std::env::var("HOME").unwrap() + "/rrfs")
}

pub fn get_tensor_by_hash_dir() -> String {
    std::env::var("TENSORS_BY_HASH_DIR")
        .map(|x| x)
        .unwrap_or_else(|_| get_rrfs_dir() + "/circuit_tensors_by_hash")
}

#[pyfunction]
pub fn tensor_from_hash(hash_base16: &str) -> Result<Tensor, PyErr> {
    let hashdir = get_tensor_by_hash_dir() + "/" + hash_base16 + ".pt";
    Python::with_gil(|py| {
        PY_UTILS
            .torch
            .getattr(py, "load")
            .unwrap()
            .call(py, (hashdir,), None)
            .map(|z| z.extract(py).unwrap())
    })
}

pub fn arrayconstant_from_hash(
    name: Option<String>,
    hash_base16: &str,
) -> Result<ArrayConstant, PyErr> {
    tensor_from_hash(hash_base16).map(|value| ArrayConstant::new(value, name))
}

#[pyfunction]
pub fn save_tensor_rrfs(tensor: Tensor) -> Result<String, PyErr> {
    let tensor = tensor.hashed();
    let hash_base16 = encode_lower(tensor.hash().unwrap());
    let hashdir = get_tensor_by_hash_dir() + "/" + &hash_base16 + ".pt";
    Python::with_gil(|py| {
        PY_UTILS
            .torch
            .getattr(py, "save")
            .unwrap()
            .call(py, (tensor.tensor(), hashdir), None)
            .map(|_| hash_base16)
    })
}

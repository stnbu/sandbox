use wasm_bindgen::prelude::*;
use std::collections::HashMap;
use serde::{Serialize, Deserialize};
use wasm_bindgen_test::*;

#[cfg(test)]
mod tests {
    use super::*;
    #[wasm_bindgen_test]
    fn it_works() {
	let json = send_example_to_js();
	assert!(!json.is_string())
    }
}

macro_rules! console_log {
    ($($t:tt)*) => (log(&format_args!($($t)*).to_string()))
}

#[wasm_bindgen(start)]
pub fn start() -> Result<(), JsValue> {
    let x = send_example_to_js();
    console_log!("Example: {:#?}", x);
    Ok(())
}

#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_namespace = console)]
    fn log(s: &str);
}

#[wasm_bindgen(inspectable)]
pub struct Baz {
    pub field: i32,
    private: i32,
}

#[wasm_bindgen]
impl Baz {
    #[wasm_bindgen(constructor)]
    pub fn new(field: i32) -> Baz {
        Baz { field, private: 13 }
    }
}

#[derive(Serialize, Deserialize)]
pub struct Example {
    pub field1: HashMap<u32, String>,
    pub field2: Vec<Vec<f32>>,
    pub field3: [f32; 4],
}

#[wasm_bindgen]
pub fn send_example_to_js() -> JsValue {
    let mut field1 = HashMap::new();
    field1.insert(0, String::from("ex"));
    let example = Example {
        field1,
        field2: vec![vec![1., 2.], vec![3., 4.]],
        field3: [1., 2., 3., 4.]
    };
    JsValue::from_serde(&example).unwrap()
}

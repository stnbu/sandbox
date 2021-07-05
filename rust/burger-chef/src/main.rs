//! 🤦

use std::collections::HashMap;
use std::convert::AsRef;
use serde_derive::{Deserialize, Serialize};

use serde_cbor::{to_vec, from_slice};

#[derive(Debug, Serialize, Deserialize)]
struct Node {
    key: String,
    children: HashMap<u32, Box<Node>>,
}

fn main() {
    let mut node_A = Node { key: "A".to_string(), children: HashMap::new() };
    let mut node_B = Node { key: "B".to_string(), children: HashMap::new() };
    let mut node_C = Node { key: "C".to_string(), children: HashMap::new() };
    let mut node_D = Node { key: "D".to_string(), children: HashMap::new() };
    let mut node_E = Node { key: "E".to_string(), children: HashMap::new() };
    let mut node_F = Node { key: "F".to_string(), children: HashMap::new() };
    let mut node_G = Node { key: "G".to_string(), children: HashMap::new() };
    let mut node_X = Node { key: "X".to_string(), children: HashMap::new() };
    let mut node_Y = Node { key: "Y".to_string(), children: HashMap::new() };
    node_F.children.insert(6, Box::new(node_G));
    node_B.children.insert(4, Box::new(node_E));
    node_B.children.insert(5, Box::new(node_F));
    node_A.children.insert(1, Box::new(node_B));
    node_A.children.insert(2, Box::new(node_C));
    node_D.children.insert(7, Box::new(node_X));
    node_D.children.insert(8, Box::new(node_Y));
    node_A.children.insert(3, Box::new(node_D));

    let bytes = to_vec(&node_A).unwrap();
    println!("Vec<u8> size: {}", bytes.len());
    let rerisen: Node = from_slice(&bytes[..]).unwrap();
    println!("TADA: {:?}", rerisen);
}

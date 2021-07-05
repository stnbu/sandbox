//! 🤦

use std::collections::HashMap;
use serde_derive::{Deserialize, Serialize};
use serde_cbor::{to_vec, from_slice};

#[derive(Debug, Serialize, Deserialize)]
struct Node {
    key: String,
    children: HashMap<u32, Box<Node>>,
}

fn main() {
    // leafs need not be `mut`
    let mut node_a = Node { key: "a".to_string(), children: HashMap::new() };
    let mut node_b = Node { key: "b".to_string(), children: HashMap::new() };
    let     node_c = Node { key: "c".to_string(), children: HashMap::new() };
    let mut node_d = Node { key: "d".to_string(), children: HashMap::new() };
    let     node_e = Node { key: "e".to_string(), children: HashMap::new() };
    let mut node_f = Node { key: "f".to_string(), children: HashMap::new() };
    let     node_g = Node { key: "g".to_string(), children: HashMap::new() };
    let     node_x = Node { key: "x".to_string(), children: HashMap::new() };
    let     node_y = Node { key: "y".to_string(), children: HashMap::new() };
    node_f.children.insert(6, Box::new(node_g));
    node_b.children.insert(4, Box::new(node_e));
    node_b.children.insert(5, Box::new(node_f));
    node_a.children.insert(1, Box::new(node_b));
    node_a.children.insert(2, Box::new(node_c));
    node_d.children.insert(7, Box::new(node_x));
    node_d.children.insert(8, Box::new(node_y));
    node_a.children.insert(3, Box::new(node_d));

    let bytes = to_vec(&node_a).unwrap();
    println!("Vec<u8> size: {}", bytes.len());
    let rerisen: Node = from_slice(&bytes[..]).unwrap();
    println!("TADA: {:?}", rerisen);
}

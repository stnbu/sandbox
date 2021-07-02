use std::collections::HashMap;
use std::convert::AsRef;
use serde_derive::{Deserialize, Serialize};

/// Trying to implement
/// [this](https://eli.thegreenplace.net/2011/09/29/an-interesting-tree-serialization-algorithm-from-dwarf)
/// in Rust with a twist: Instead of just having a "list" of children, we have the children in a `HashMap`, indexed by a number (their distance, in a HKTree).

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

    node_F.children.insert(6, &node_G);
    node_B.children.insert(4, &node_E);
    node_B.children.insert(5, &node_F);
    node_A.children.insert(1, &node_B);
    node_A.children.insert(2, &node_C);
    node_D.children.insert(7, &node_X);
    node_D.children.insert(8, &node_Y);
    node_A.children.insert(3, &node_D);

    let chars = to_bytes(&node_A).iter().map(|value| *value as char).collect::<Vec<_>>();
    for ch in chars {
	print!("{}", ch);
    }
    println!("");
}

fn ser(key: String) -> Vec<u8> {
    key.into_bytes()
}

fn to_bytes(root: &Node) -> Vec<u8> {
    let mut mem: Vec<u8> = Vec::new();
    fn serialize (pdist: u32, node: &Node, mem: &mut Vec<u8>) {
	// The following append the node "data" (32-bit distance + literal bytes of key)
	//mem.extend(&pdist.to_ne_bytes());
	let key_data = ser(node.key.clone());
	if !node.children.is_empty() {
	    mem.extend(&key_data[..]); mem.push(b'v'); // children follow
	    for (dist, child_node) in node.children.iter() {
		serialize(*dist, child_node, mem);
	    }
	    mem.push(b'<'); // end children
	} else {
	    mem.extend(&key_data[..]); mem.push(b'>'); // zero or more siblings follow.
	}
    }
    serialize(0, &root, &mut mem);
    mem
}


// How to interpret the data that follows the current node, _with respect to the current node_.
#[derive(Debug, Serialize, Deserialize)]
enum Next {
    Child, // the node that follows is the current node's child
    Sibling, // the node that follows is the current node's sibling
}

// This will be a value we get from a HashMap of locations in the data.
#[derive(Debug, Serialize, Deserialize)]
struct NodeRecordLayout {
    size: usize,
    next_comes: Next,
}

// Gets encoded and placed at the beginning of the serialization output.
#[derive(Debug, Serialize, Deserialize)]
struct OutputPrefix {
    boundries: HashMap<usize, Option<NodeRecordLayout>>,
}

#[derive(Debug)]
struct Node<'a> {
    key: String,
    children: HashMap<u32, &'a Node<'a>>,
}

impl<'a> AsRef<Node<'a>> for Node<'a> {
    fn as_ref(&self) -> &Self {
        self
    }
}

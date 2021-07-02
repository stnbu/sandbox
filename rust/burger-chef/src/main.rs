use std::collections::HashMap;
use std::convert::AsRef;
use serde_derive::{Deserialize, Serialize};

use serde_cbor::to_vec;

/// Trying to implement
/// [this](https://eli.thegreenplace.net/2011/09/29/an-interesting-tree-serialization-algorithm-from-dwarf)
/// in Rust with a twist: Instead of just having a "list" of children, we have the children in a `HashMap`, indexed by a number (their distance, in a HKTree).

fn main() {

    let mut node_A = Node { key: "A".to_string(), children: HashMap::new() };
    let mut node_C = Node { key: "C".to_string(), children: HashMap::new() };

    node_A.children.insert(2, &node_C);

    let chars = to_bytes(&node_A).iter().map(|value| *value as char).collect::<Vec<_>>();
    for ch in chars {
	print!("{}", ch);
    }
    println!("");
}

fn to_bytes(root: &Node) -> Vec<u8> {
    let mut header = Header {
	records: Vec::new(),
    };
    let mut mem: Vec<u8> = Vec::new();
    fn serialize (pdist: u32, node: &Node, mem: &mut Vec<u8>, header: &mut Header) {
	let offset = mem.len();
	let mut next;

	mem.extend(to_vec(&pdist).unwrap());
	mem.extend(to_vec(&node.key).unwrap());

	if !node.children.is_empty() {
	    next = Next::Child;
	    for (dist, child_node) in node.children.iter() {
		serialize(*dist, child_node, mem, header);
	    }
	    //next = Next::Pop; // so confuse. how do I encode "pop up one level here er whatever"
	} else {
	    next = Next::Sibling;
	}
	let size = mem.len() - offset;
	header.records.push(Record {
	    offset,
	    size,
	    next,
	});
    }
    serialize(0, &root, &mut mem, &mut header);

    // create serialized header, measure len()

    let _header_bytes = to_vec(&header);

    // MutMap to increment all "offset" by the above size.



    // Easy to miss, subtle to understand! We serialize by starting at root and discending to leaves.
    // Since, when we DEserialize, we must build the tree from the leaves to the root, we just flip
    // this vector right here and only mention so here. The deserialization code need only follow the
    // vec and assemble the tree, as one would expect. probably.
    header.records = header.records.into_iter().rev().collect::<Vec<_>>(); // FIXME: problem! memory.
    println!("HEADER: {:?}", header);
    mem
}


// How to interpret the data that follows the current node, _with respect to the current node_.
#[derive(Debug, Serialize, Deserialize)]
enum Next {
    Child,   // the node that follows is the current node's child
    Sibling, // the node that follows is the current node's sibling
    Pop,     // I know, right? Not "father" but the instruction is to "pop", meaning end-of-children.
}

// This will be a value we get from a HashMap of locations in the data.
#[derive(Debug, Serialize, Deserialize)]
struct Record {
    offset: usize,
    size: usize,
    next: Next,
}

// Gets encoded and placed at the beginning of the serialization output.
#[derive(Debug, Serialize, Deserialize)]
struct Header {
    records: Vec<Record>,
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

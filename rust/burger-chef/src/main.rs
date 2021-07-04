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

// We serialize an HKTree in the following way:
// 1. Starting with the root node, recursively follow each node and write out bytes
// ```
// <distance><node_key>
// ```
// where `distance` is the distance (`u32`) to the node's parent and `node_key` is the binary encoding of the node's key.
// 2. During the above, we record a record for each node in a `Record` struct. We record
//   * `offset` - location in the stream of the beginning of the encoded node
//   * `size` - length of encoded node in bytes
//   * `next` - How to interpret the next record (child, sibling, end of siblings)
// 3. Reverse the records, because the tree must be constructed in the opposite order.
// 4. Create a `Header` struct using the above records as its `records` field.
// 5. Measure the size of the encoded header, and increment the `offset` of each node by the header's size, since the
// header is prepended to the stream.
// 6. Create and return a `result: Vec<8>` by concatenating the encoded header and encoded node streams.
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

    let mut header_bytes = to_vec(&header).unwrap();
    let header_size = header_bytes.len();

    // We serialize  by starting at root and  descending to leaves. Since,  when we DEserialize, we must  build the tree
    // from the leaves to  the root, we just flip this vector right here. The  deserialization code need only follow the
    // vec and assemble the tree, as one would expect. probably.
    header.records = header.records.into_iter().rev().collect::<Vec<_>>(); // FIXME: problem! memory.

    let shifted_records: Vec<Record> = header.records.into_iter().map(|x| Record {
	offset: x.offset + header_size,
	..x
    }).collect();

    let mut result: Vec<u8> = Vec::new();

    result.append(&mut header_bytes);
    result.append(&mut mem);
    result
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

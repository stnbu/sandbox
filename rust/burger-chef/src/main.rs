use std::collections::HashMap;
use std::convert::AsRef;
use serde_derive::{Deserialize, Serialize};

use serde_cbor::{to_vec, from_slice};

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

    //let mut chars = to_bytes(&node_A).iter().map(|value| *value as char).collect::<Vec<_>>();
    // for (i, ch) in chars.iter().enumerate() {
    // 	println!("{:06}:{}", i, ch);
    // }
    // println!("");
}

//fn print_vec8(v: &Vec<u8>) {
fn print_vec8(v: &[u8]) {
    for ch in v {
	print!("{}", *ch as char);
    }
    println!("");
}

/// We serialize an HKTree in the following way:
/// 1. Starting with the root node, recursively follow each node and write out bytes
/// ```
/// <distance><node_key>
/// ```
/// where `distance` is the distance (`u32`) to the node's parent and `node_key` is the serialized node key.
/// 2. During the above, we record a record for each node in a `Record` struct. We record
///   * `offset` - location in the stream of the beginning of the encoded node
///   * `size` - length of encoded node in bytes
///   * `next` - How to interpret the next record (child, sibling, end of siblings)
/// 3. Reverse the records, because the tree must be constructed in the opposite order.
/// 4. Create a `Header` struct using the above records as its `records` field.
/// 5. Measure the size of the encoded header, and increment the `offset` of each node by the header's size, since the
/// header is prepended to the stream.
/// 6. Create and return a `result: Vec<8>` by concatenating the encoded header and encoded node streams.
fn to_bytes(root: &Node) -> Vec<u8> {
    fn serialize (pdist: u32, node: &Node, node_stream_bytes: &mut Vec<u8>, header: &mut Header) {
	let offset = node_stream_bytes.len();
	let mut next;
	node_stream_bytes.extend(to_vec(&pdist).unwrap());
	node_stream_bytes.extend(to_vec(&node.key).unwrap());
	if !node.children.is_empty() {
	    next = Some(Next::Child);
	    for (dist, child_node) in node.children.iter() {
		serialize(*dist, child_node, node_stream_bytes, header);
		next = None;
	    }
	} else {
	    next = Some(Next::Sibling);
	}
	let size = node_stream_bytes.len() - offset;
	header.records.push(Record {
	    offset,
	    size,
	    next,
	});
    }

    let pdist = 0u32; // root has no parent and therefore no distance. We waste four bytes for consistency's sake.
    let mut node_stream_bytes: Vec<u8> = Vec::new();
    let mut header = Header { records: Vec::new() };
    serialize(pdist, &root, &mut node_stream_bytes, &mut header);

    // Save the size the serialized header, _will be_. Changes are made below, but the size does not change.
    let header_size: u8 = to_vec(&header).unwrap().len() as u8;
    println!("serialization header size: {}", &header_size);
    // We serialize  by starting at root and  descending to leaves. Since,  when we DEserialize, we must  build the tree
    // from the leaves to  the root, we just flip this vector right here. The deserialization code need only follow the
    // vec and assemble the tree, as one would expect.
    header.records = header.records.into_iter().rev().collect::<Vec<_>>(); // FIXME: problem! memory.
    // The header goes ahead of the node stream, so we increment each record by the size of the seralized header.
    // Importantly, this does not change the size of the header.
    header.records = header.records.into_iter().map(|x| Record {
	offset: x.offset + header_size as usize + 1, // Because we prefix the whole thing with header length.
	..x
    }).collect(); // FIXME: again, memory. This shold be doable in-place.
    let mut header_bytes = to_vec(&header).unwrap();

    let mut result: Vec<u8> = vec![];
    result.append(&mut node_stream_bytes);
    result.append(&mut header_bytes);
    result.push(header_size);
    result
}

fn from_bytes<'a>(bytes: &mut Vec<u8>) -> Node<'a> {
    let fork = false;
    if fork {
	for ch in bytes {
	    println!(" ===> {}", ch);
	    break;
	}
    } else {
	let header_size: u8 = bytes.pop().unwrap().into();
	println!(" ===>  {}", header_size);
    }

    //let elems: &[u8] = &bytes[bytes.len() - header_size ..]; //.into().unwrap();
    //print_vec8(elems);
    // let header: Header = from_slice(elems).unwrap();
    // bytes.truncate(bytes.len() - header_size);

    Node { children: HashMap::new(), key: "x".to_string() }
}


// How to interpret the data that follows the current node, _with respect to the current node_.
#[derive(Debug, Serialize, Deserialize)]
enum Next {
    Child,   // the node that follows is the current node's child
    Sibling, // the node that follows is the current node's sibling
}

// This will be a value we get from a HashMap of locations in the data.
#[derive(Debug, Serialize, Deserialize)]
struct Record {
    offset: usize,
    size: usize,
    next: Option<Next>,
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

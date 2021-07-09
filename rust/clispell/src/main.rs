//! Pass a single command line argument <word> and have all words of distance=1 printed.

use bk_tree::{BKTree, BKNode, metrics};
use std::env;
use std::io::prelude::*;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
	println!("Usage: {} <word>", &args[0]);
	return ();
    }
    let tree = get_tree();
    for result in tree.find(&args[1], 1) {
	println!("{}", result.1);
    }
}

fn get_tree() -> BKTree<String> {
    if !Path::new("dict.dat").exists() {
	eprintln!("Performing a one-time import of the words file...");
	let mut tree: BKTree<String> = BKTree::new(metrics::Levenshtein);
	let filename = "/usr/share/dict/words";
	let file = File::open(filename).unwrap();
	let lines = io::BufReader::new(file).lines();
	for line in lines {
	    tree.add(line.unwrap().to_lowercase());
	}
	let bytes = &tree.root.unwrap().to_vec().unwrap();
	write_serialized_bknode(bytes);
	assert!(Path::new("dict.dat").exists());
    };
    let bytes = read_serialized_bknode();
    match BKNode::from_slice(&bytes) {
	Ok(node) => {
	    let mut tree: BKTree<String> = BKTree::new(metrics::Levenshtein);
	    tree.root = Some(node);
	    tree
	},
	Err(e) => {
	    panic!("Deserialize Err: {}", e);
	},
    }
}

fn write_serialized_bknode(bytes: &Vec<u8>) {
    let path = Path::new("dict.dat");
    let mut file = match File::create(&path) {
        Err(e) => panic!("Create Err: {}", e),
        Ok(file) => file,
    };
    match file.write_all(&bytes) {
        Err(e) => panic!("Write Err: {}", e),
        Ok(_) => {},
    }
}

fn read_serialized_bknode() -> Vec<u8> {
    let path = Path::new("dict.dat");
    let mut file = match File::open(&path) {
        Err(e) => panic!("Open Err: {}", e),
        Ok(file) => file,
    };
    let mut result: Vec<u8> = Vec::new();
    let _ = file.read_to_end(&mut result);
    result
}

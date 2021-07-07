use bk_tree::{BKTree, BKNode, metrics};

use std::io::prelude::*;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // Deserialize existing file into BKTree
    let bytes = read();
    let tree = match BKNode::from_slice(&bytes) {
	Ok(node) => {
	    let mut tree: BKTree<String> = BKTree::new(metrics::Levenshtein);
	    tree.root = Some(node);
	    tree
	},
	Err(why) => { println!("deserialize error: {:?}", why); return; },
    };
    return ();
    
    // Build BKTree by iterating word file
    let mut tree: BKTree<String> = BKTree::new(metrics::Levenshtein);
    let filename = "/usr/share/dict/words";
    let file = File::open(filename).unwrap();
    let lines = io::BufReader::new(file).lines();
    for line in lines {
	tree.add(line.unwrap().to_lowercase());
    }

    // Write (a) BKTree to disk.
    let bytes = &tree.root.unwrap().to_vec().unwrap();
    write(bytes);
}


fn write(bytes: &Vec<u8>) {
    let path = Path::new("dict.dat");
    let mut file = match File::create(&path) {
        Err(why) => panic!("Create Err: {}", why),
        Ok(file) => file,
    };
    match file.write_all(&bytes) {
        Err(why) => panic!("Write Err: {}", why),
        Ok(_) => {},
    }
}

fn read() -> Vec<u8> {
    let path = Path::new("dict.dat");
    let mut file = match File::open(&path) {
        Err(why) => panic!("Open Err: {}", why),
        Ok(file) => file,
    };
    let mut result: Vec<u8> = Vec::new();
    let _ = file.read_to_end(&mut result);
    result
}

//! A simple spellcheck library.
//!
//! Using the system `words` file, build a bktree using word distance. Use that for lookups of spellcheck suggestions.
//! The resulting `bk_tree` is stored to disk after a one-time processing, so startup loading overhead goes from minutes
//! sub-second.
//!
//! Word distance is calculated using the Levenshtein metric.

use bk_tree::{BKTree, BKNode, metrics};
use std::io::prelude::*;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

static BKTREE_STORE_FILE: &str = "./words-bk-tree.bin";
static SYSTEM_WORD_FILE: &str = "/usr/share/dict/words";
static SEARCH_DISTANCE: u32 = 1;

/// Pass your query `word` and get a `Vec<String>` of words that are `odistance` or nearer your word.
pub fn search(word: &str, odistance: Option<u32>) -> Result<Vec<String>, &str> {
    let distance: u32 = match odistance {
	None => SEARCH_DISTANCE,
	Some(d) => d,
    };
    let tree = get_tree();
    Ok(tree.find(word, distance).map(|pair| {pair.1.to_string()}).collect())
}

fn get_tree() -> BKTree<String> {
    if !Path::new(BKTREE_STORE_FILE).exists() {
	eprintln!("Performing a one-time import of the words file...");
	let mut tree: BKTree<String> = BKTree::new(metrics::Levenshtein);
	let file = File::open(SYSTEM_WORD_FILE).unwrap();
	let lines = io::BufReader::new(file).lines();
	for line in lines {
	    tree.add(line.unwrap().to_lowercase());
	}
	let bytes = &tree.root.unwrap().to_vec().unwrap();
	write_serialized_bknode(bytes);
	assert!(Path::new(BKTREE_STORE_FILE).exists());
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
    let path = Path::new(BKTREE_STORE_FILE);
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
    let path = Path::new(BKTREE_STORE_FILE);
    let mut file = match File::open(&path) {
        Err(e) => panic!("Open Err: {}", e),
        Ok(file) => file,
    };
    let mut result: Vec<u8> = Vec::new();
    let _ = file.read_to_end(&mut result);
    result
}

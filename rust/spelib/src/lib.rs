/*

Hello, future person. I am past Mike. I strategically dropped this thing.

If your memory need jogging. This is a simple, toy "spellchecking suggestions" library `mysearchtree.search("bureaucrasy", 1);` (second arg is the distance).

It returns a `Vec<String>` of results with specified distance.
The "hard part" is messing around with reading (words file) and writing (serialized tree binary) files.
I got twisted about trying to "return two different kinds of errors" for a `Result` `Err` variant. Which is solved
[here](https://doc.rust-lang.org/std/convert/trait.From.html#examples) if you care to adapt. Someone else suggested `anyhow` so that's why it's in the deps, unexplored, unimplemented.
The bigger picture (the parent toy program) was going to be a `Rocket` spellcheck "API": `GET /search/myword` -> get a JSON array of suggestions. Also, as a "funny" twist, I thought of having an option to specifically return the _most distant_
words. Suggest "flower", get "disestablishmentarianism" as a result...

*/
//! A simple spellcheck library.
//!
//! Using the system `words` file, build a bktree using word distance. Use that for lookups of spellcheck suggestions.
//! The resulting `bk_tree` is stored to disk after a one-time processing, so startup loading overhead goes from minutes
//! sub-second.
//!
//! Word distance is calculated using the Levenshtein metric.

use bk_tree::{metrics, BKNode, BKTree};
use std::fs::File;
use std::io::prelude::*;
use std::io::{self, BufRead};
use std::path::Path;
//use anyhow::Result;

static BKTREE_STORE_FILE: &str = "./words-bk-tree.bin";
static SYSTEM_WORD_FILE: &str = "/usr/share/dict/words";
static SEARCH_DISTANCE: u32 = 1;

pub struct SearchTree {
    tree: BKTree<String>,
}
//use std::error::Error;

impl SearchTree {
    /// Pass your query `word` and get a `Vec<String>` of words that are `odistance` or nearer your word.
    pub fn search<'a>(&self, word: &str, odistance: Option<u32>) -> Result<Vec<String>, &'a str> {
        let distance: u32 = match odistance {
            None => SEARCH_DISTANCE,
            Some(d) => d,
        };
        let mut results: Vec<String> = Vec::new();
        for (_, result) in self.tree.find(word, distance) {
            results.push(result.to_string());
        }
        Ok(results)
    }
    pub fn new_from_words_path() -> Result<Self, std::io::Error> {
        let mut tree: BKTree<String> = BKTree::new(metrics::Levenshtein);
        let file = File::open(SYSTEM_WORD_FILE)?;
        let lines = io::BufReader::new(file).lines();
        for line in lines {
            tree.add(line.unwrap().to_lowercase());
        }
        Ok(Self { tree })
    }
    pub fn new_from_serialized_path(path: &Path) -> anyhow::Result<Self> {
        let file = File::open(&path)?;
        let mut bytes: Vec<u8> = Vec::new();
        let _ = file.read_to_end(&mut bytes);
        Self::new_from_bytes(&bytes)
    }
    pub fn new_from_bytes(bytes: &[u8]) -> Result<Self, serde_cbor::error::Error> {
        match BKNode::from_slice(bytes) {
            Ok(node) => {
                let mut tree: BKTree<String> = BKTree::new(metrics::Levenshtein);
                tree.root = Some(node);
                Ok(Self { tree })
            }
            Err(e) => Err(e),
        }
    }
    pub fn write_to_path(&self, path: &Path) -> Result<u32, std::io::Error> {
        let bytes = &self.tree.root.unwrap().to_vec()?;
        let mut file = match File::create(&path) {
            Err(e) => panic!("Create Err: {}", e),
            Ok(file) => file,
        };
        file.write_all(&bytes)?
    }
}

#[cfg(test)]
mod tests {
    use crate::{SearchTree, BKTREE_STORE_FILE};
    use std::path::Path;

    #[test]
    fn test_all() {
        //use std::fs;
        //fs::remove_file(BKTREE_STORE_FILE).ok();
        let path = Path::new(BKTREE_STORE_FILE);
        let foo = path;
        let tree = SearchTree::new_from_serialized_path(&path);
        let results: Vec<String> = tree
            .unwrap()
            .search("robert", None)
            .unwrap()
            .into_iter()
            .collect();
        assert!(results.len() == 5)
    }
}

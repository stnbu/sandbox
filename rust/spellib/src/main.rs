use bk_tree::{BKTree, metrics};

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut tree: BKTree<String> = BKTree::new(metrics::Levenshtein);
    let filename = "/usr/share/dict/words";
    let file = File::open(filename).unwrap();
    let lines = io::BufReader::new(file).lines();
    println!("Composing BKTree...");
    for (index, line) in lines.enumerate() {
	println!("{}", 235886 - index);
	tree.add(line.unwrap().to_lowercase());
    }
    let size = std::mem::size_of_val(&tree);
    println!("\nDone! ({} bytes)", size);

    let benchlike = tree.find("bench", 2).collect::<Vec<_>>();
    println!("distance-2 from bench: {:?}", benchlike)
}

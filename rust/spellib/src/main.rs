use bk_tree::{BKTree, metrics};

use serde_derive::{Deserialize, Serialize};
use std::error::Error;

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

#[derive(Debug, Serialize, Deserialize)]
struct StringBKTree {
    tree: BKTree<String>
}

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



// fn main2() -> Result<(), Box<dyn Error>> {
//     let ferris = Mascot {
//         name: "Ferris".to_owned(),
//         species: "crab".to_owned(),
//         year_of_birth: 2015,
//     };

//     let ferris_file = File::create("words.cbor")?;
//     serde_cbor::to_writer(ferris_file, &ferris)?;

//     let tux_file = File::open("words.cbor")?;
//     let tux: Mascot = serde_cbor::from_reader(tux_file)?;

//     println!("{:?}", tux);

//     Ok(())
// }

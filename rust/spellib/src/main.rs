use bk_tree::{BKTree, BKNode, metrics};

use std::error::Error;

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut tree: BKTree<String> = BKTree::new(metrics::Levenshtein);

    let bytes = read();
    //println!(" --> {:?}", bytes);
    let x = match BKNode::from_slice(&bytes) {
	Ok(node) => {
	    println!("Oh nooode!");
	    node
	},
	Err(why) => { println!("deserialize error: {:?}", why); return; },
    };

    tree.root = Some(x);
    //println!("--> {:?}", &tree);
    let benchlike = tree.find("bench", 2).collect::<Vec<_>>();
    println!("distance-2 from bench: {:?}", benchlike);

    return (());
    
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

    let bytes = &tree.root.unwrap().to_vec().unwrap();
    write(bytes);
    //println!("serialized bytes: {}", bytes.len());

    // let benchlike = tree.find("bench", 2).collect::<Vec<_>>();
    // println!("distance-2 from bench: {:?}", benchlike)
}

//use std::fs::File;
use std::io::prelude::*;
//use std::path::Path;

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
    let bytes_read = file.read_to_end(&mut result);
    result
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

use bk_tree::BKTree;
//use bk_tree::serde_cbor;

fn main() {
    let mut tree: BKTree<&str> = Default::default();
    tree.add("book");
    tree.add("book");
    println!("Bodes: {:?}", tree.find("", 4).collect::<Vec<_>>());
    let bytes = &tree.to_vec().unwrap();
    println!("Serialized: {:?}", &bytes);
    // let tree = BKTree::<&str>::from_slice(&bytes, bk_tree::metrics::Levenshtein);
    // println!("Tree: {:?}", tree);
}

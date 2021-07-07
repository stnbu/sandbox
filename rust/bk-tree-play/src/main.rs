use bk_tree::BKTree;
//use bk_tree::serde_cbor;

fn main() {
    let mut tree: BKTree<String> = Default::default();
    tree.add("book".to_string());
    //tree.add("book");
    println!("Bodes: {:?}", tree.find("", 4).collect::<Vec<_>>());
    let bytes = &tree.to_vec().unwrap();
    //println!("Serialized: {:?}", &bytes);
    let tree: Result<BKTree<String>, serde_cbor::error::Error> = BKTree::from_slice(&bytes.as_ref().unwrap()[..], bk_tree::metrics::Levenshtein);
    println!("Tree: {:?}", tree);
}

use bk_tree::{BKNode, BKTree};
//use bk_tree::serde_cbor;

fn main() {
    let mut tree: BKTree<String> = Default::default();
    tree.add("book".to_string());
    //tree.add("book");
    println!("Bodes: {:?}", tree.find("", 4).collect::<Vec<_>>());
    let bytes = &tree.root.unwrap().to_vec().unwrap();
    //println!("Serialized: {:?}", &bytes);
    let node: BKNode<String> = BKNode::from_slice(&bytes).unwrap();
    println!("Tree: {:?}", node);
}

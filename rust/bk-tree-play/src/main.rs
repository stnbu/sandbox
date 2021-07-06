use bk_tree::BKTree;
fn main() {
    let mut tree: BKTree<&str> = Default::default();
    tree.add("book");
    tree.add("book");
    println!("{:?}", tree.find("", 4).collect::<Vec<_>>());
}

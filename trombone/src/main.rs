fn main() {
    let query = "two";
    let contents = "one two three\nfour five six";
    let results = search(&query, &contents);
    println!("results: {:?}", results);
}
// &'a std::str::Lines<'a> {
fn search<'a>(query: &str, contents: &'a str) -> std::iter::Filter<&str, |&str| &str> {
    contents
        .lines()
        .filter(|line| line.contains(query))
}

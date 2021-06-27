use rocket::tokio::time::{sleep, Duration};
use std::path::{Path, PathBuf};
use rocket::fs::NamedFile;
use rocket::http::Status;
use rocket::response::{content, status};
use std::sync::atomic::Ordering;
use std::sync::atomic::AtomicUsize;
use rocket::State;

//// For now, we support one word. We would like, e.g.
////   /word1/word2/... (silly but looks nice)
////   /?word2&word2&... (probably no less silly, actually)
#[rocket::get("/<word>")]
fn spell(word: &str) -> content::Json<&'static str> {
    println!("[INFO] Hey, this guy cannot spell \"{}\". LOL!", word);
    content::Json("{ \"suggestion\": \"<buy a dictionary?>\" }")
}

fn get_sugggestions(word: &str) -> Vec<&str> {
    let ten_millis = std::time::Duration::from_millis(10);
    std::thread::sleep(ten_millis);
    vec!["maybe this", "or maybe this"]
}

#[rocket::main]
async fn main() {
    let _ = rocket::build()
        .mount("/", rocket::routes![spell])
        .launch()
        .await;
}

use rocket::tokio::time::{sleep, Duration};
use std::path::{Path, PathBuf};
use rocket::fs::NamedFile;
use rocket::http::Status;
use rocket::response::{content, status};
use std::sync::atomic::Ordering;
use std::sync::atomic::AtomicUsize;
use rocket::State;

#[rocket::get("/<word>")]
fn hello(word: &str) -> String {
    format!("You cannot spell _{}_ ?!", String::from(word).to_uppercase()) // does not _feel_ right
}

#[rocket::main]
async fn main() {
    let _ = rocket::build()
        .mount("/", rocket::routes![hello])
        .launch()
        .await;
}

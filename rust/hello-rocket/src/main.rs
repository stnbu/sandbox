use rocket::tokio::time::{sleep, Duration};
use std::path::{Path, PathBuf};
use rocket::fs::NamedFile;
use rocket::http::Status;
use rocket::response::{content, status};
use std::sync::atomic::Ordering;
use std::sync::atomic::AtomicUsize;
use rocket::State;

#[rocket::get("/")]
fn hello() -> &'static str {
    "Hello, world!"
}

#[rocket::get("/teapot")]
fn teapot() -> status::Custom<content::Json<&'static str>> {
    status::Custom(Status::ImATeapot, content::Json("{ \"hi\": \"world\" }"))
}

/////// TODO: The plan here was to print the number of segmens. Do you know how to do that _now_?
// #[rocket::get("segments/<segments..>/end")]
// fn hello(segments: &[str]) -> &'static str {
//     ""
// }

#[rocket::get("/delay/<seconds>")]
async fn delay(seconds: u64) -> String {
    println!("waiting for {} seconds", seconds);
    sleep(Duration::from_secs(seconds)).await;
    println!("...done");
    format!("Waited for {} seconds", seconds)
}

#[rocket::get("/hello/<name>/<age>/<cool>")]
fn arbitrary(name: &str, age: u8, cool: bool) -> String {
    if cool {
        format!("You're a cool {} year old, {}!", age, name)
    } else {
        format!("{}, we need to talk about your coolness.", name)
    }
}


#[rocket::get("/files/<file..>")]
async fn files(file: PathBuf) -> Option<NamedFile> {
    NamedFile::open(Path::new("static/").join(file)).await.ok()
}

// #[rocket::launch]
// fn rocket() -> _ {
//     rocket::build().mount("/", rocket::routes![hello])
// }

struct HitCount {
    count: AtomicUsize
}

#[rocket::get("/count")]
fn count(hit_count: &State<HitCount>) -> String {
    let current_count = hit_count.count.load(Ordering::Relaxed);
    // Ok, but this doesn't increment
    format!("Number of visits: {}", current_count)
}

#[rocket::main]
async fn main() {
    let _ = rocket::build()
        .mount("/", rocket::routes![delay, arbitrary, files, teapot, count, hello])
	.manage(HitCount { count: AtomicUsize::new(0) })
        .launch()
        .await;
}

use rocket::tokio::time::{sleep, Duration};

#[rocket::get("/")]
fn hello() -> &'static str {
    "Hello, world!"
}

#[rocket::get("/delay/<seconds>")]
async fn delay(seconds: u64) -> String {
    println!("waiting for {} seconds", seconds);
    sleep(Duration::from_secs(seconds)).await;
    println!("...done");
    format!("Waited for {} seconds", seconds)
}

// #[rocket::launch]
// fn rocket() -> _ {
//     rocket::build().mount("/", rocket::routes![hello])
// }

#[rocket::main]
async fn main() {
    let _ = rocket::build()
        .mount("/", rocket::routes![delay])
        .launch()
        .await;
}

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

#[rocket::get("/hello/<name>/<age>/<cool>")]
fn arbitrary(name: &str, age: u8, cool: bool) -> String {
    if cool {
        format!("You're a cool {} year old, {}!", age, name)
    } else {
        format!("{}, we need to talk about your coolness.", name)
    }
}

// #[rocket::launch]
// fn rocket() -> _ {
//     rocket::build().mount("/", rocket::routes![hello])
// }

#[rocket::main]
async fn main() {
    let _ = rocket::build()
        .mount("/", rocket::routes![delay, arbitrary])
        .launch()
        .await;
}


#[rocket::get("/")]
fn hello() -> &'static str {
    "Hello, world!"
}

// #[rocket::launch]
// fn rocket() -> _ {
//     rocket::build().mount("/", rocket::routes![hello])
// }

#[rocket::main]
async fn main() {
    let _ = rocket::build()
        .mount("/", rocket::routes![hello])
        .launch()
        .await;
}

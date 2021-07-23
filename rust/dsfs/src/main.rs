
use rocket_contrib::serve::StaticFiles;
fn main() {
    rocket::ignite()
        .mount("/public", StaticFiles::from("/static"))
        .launch();
}


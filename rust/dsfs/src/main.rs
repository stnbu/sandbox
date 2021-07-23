/// `dsfs`
///
/// The "missing" rust webdev utility server (pre-alpha)
///
/// If you cannot `cargo install dsfs`, I have failed. The quality to improve!
///
/// It re-uses existing tools and is dead-simple as a "feature".
///
/// ```
/// dsfs ./   # serves current directory at localhost:8000
/// dsfs      # serves current directory at localhost:8000
/// dsfs /tmp # serves /tmp/ localhost:8000
/// ```

use std::env;
use rocket_contrib::serve::StaticFiles;

fn main() {
    let args: Vec<String> = env::args().collect();
    let path = match args.len() {
	1 => "./",
	2 => &args[1],
	_ => panic!("Usage: {} [path]\n\tServe content of `path` directiory at localhost:8000",
		    args[0]),
    };
    rocket::ignite()
        .mount("/", StaticFiles::from(path))
        .launch();
}


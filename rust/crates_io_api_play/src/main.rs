/// Verbatim example code from `crates_io_api` docs. Just for fun.

use crates_io_api::{SyncClient, Error};

fn list_top_dependencies() -> Result<(), Error> {
    // Instantiate the client.
    let client = SyncClient::new(
         "test-crates-io-api (mb@unintuitive.org)",
         std::time::Duration::from_millis(1000),
    )?;
    // Retrieve summary data.
    let summary = client.summary()?;
    for c in summary.most_downloaded {
        println!("{}:", c.id);
        for dep in client.crate_dependencies(&c.id, &c.max_version)? {
            // Ignore optional dependencies.
            if !dep.optional {
                println!("    * {} - {}", dep.id, dep.version_id);
            }
        }
    }
    Ok(())
}

fn main() {
    let _ = list_top_dependencies().expect("I did NOT expect this");
}

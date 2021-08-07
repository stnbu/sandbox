
use clap::{Arg, App};

// // #![allow(unused)]
// // #![feature(str_split_as_str)]
// fn main2() {
//     let mut split = "1.2.3.4:9000".split(':');
//     let ip = split.next().unwrap_or("0.0.0.0");
//     let port = split.next().unwrap_or("8000");
//     println!("addr: {}", address);
//     println!("port: {}", port);
//     // for x in split {
//     // 	dbg!(x);
//     // }
//     //dbg!();
//     // assert_eq!(split.as_str(), "Mary had a little lamb");
//     // split.next();
//     // assert_eq!(split.as_str(), "had a little lamb");
//     // split.by_ref().for_each(drop);
//     // assert_eq!(split.as_str(), "");
// }

fn main() {
    let matches = App::new("Dead Simple File Server")
                          .version(clap::crate_version!())
                          .author(clap::crate_authors!())
                          .arg(Arg::with_name("address")
                               .short("a")
                               .long("address")
                               .value_name("IPV4_ADDR")
                               .help("An IPv4 address of the form a.b.c.d:1234")
                               .takes_value(true))
	                  .arg(Arg::with_name("path")
                               .index(1))
                          .get_matches();
    let address = matches.value_of("address").unwrap_or("0.0.0.0:8000");
    let path = matches.value_of("path").unwrap_or(".");

    let mut split = address.split(":");
    let ip = split.next().unwrap_or("0.0.0.0");
    let port = split.next().unwrap_or("8000");
    println!("ip  : {}", ip);
    println!("port: {}", port);
    println!("path: {}", path);
}

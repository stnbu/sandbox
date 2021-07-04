use serde_derive::{Deserialize, Serialize};
use serde_cbor::{to_vec, from_slice};

#[derive(Debug, Serialize, Deserialize)]
struct Foo {
    value: u32,
}

// CBOR round-trip example.
fn main() {
    let foo = Foo { value: 9 };
    let bytes = to_vec(&foo).unwrap();
    let foo_resurected: Foo = from_slice(&bytes[..]).unwrap();
    println!("{:?}", foo_resurected);
}

// that time I learned that U256 implements the From bound.

use web3::types::U256;

fn main() {
    let x: Option<U256> = Some(5.into());
    println!("into: {:?}", x);
}

/// * This is usful and took some time to grok
/// * It introduces `impl` in a context that might be new and was to me.
/// * It allows you to specify one of two types in function artuments.
/// * Could it be extended for your own enum `Some(u32) || Some(&str) || Some(Vec<u8>) || None` ...?

// thank you, sir: https://discord.com/channels/273534239310479360/273541522815713281/865704536287084555
fn test(x: impl Into<Option<u32>>) {
    match x.into() {
        Some(n) => println!("got {:?}", n),
        None => println!("got None"),
    }
}

fn main() {
    test(3);
    test(None);
}

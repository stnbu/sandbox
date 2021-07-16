/// * Practical use of the Into trait.
/// * One way to generalzie returned errors.

// thank you, sir: https://discord.com/channels/273534239310479360/273541522815713281/865704536287084555
fn test(x: impl Into<Option<u8>>) {
    match x.into() {
        Some(n) => println!("got {}", n),
        None => println!("got None"),
    }
}

fn main() {
    test(3);
    test(None);
}

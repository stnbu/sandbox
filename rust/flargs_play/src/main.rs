/// * Practical use of the From trait.
/// * One way to generalzie returned errors.

#[derive(Debug)]
enum VaryInt {
    Some(u8)
}

impl From<u8> for VaryInt {
    fn from(value: u8) -> Self {
        Self::Some(value)
    }
}

impl From<Option<u8>> for VaryInt {
    fn from(o: Option<u8>) -> Self {
	match o {
	    Some(value) => {
		VaryInt::Some(value)
	    },
	    None => {
		VaryInt::Some(0)
	    },
	}
    }
}

fn test(x: VaryInt) {
    println!("--> {:?}", x);
}

fn main() {
    test(None);
    test(3);
}

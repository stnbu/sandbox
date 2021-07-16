/// * Practical use of the From trait.
/// * One way to generalzie returned errors.

use std::fs;
use std::io;
use std::num;

#[derive(Debug)]
enum CliError {
    IoError(io::Error),
    ParseError(num::ParseIntError),
}

impl From<io::Error> for CliError {
    fn from(error: io::Error) -> Self {
        CliError::IoError(error)
    }
}

impl From<num::ParseIntError> for CliError {
    fn from(error: num::ParseIntError) -> Self {
        CliError::ParseError(error)
    }
}

fn open_and_parse_file(file_name: &str) -> Result<i32, CliError> {
    let mut contents = fs::read_to_string(&file_name)?;
    let num: i32 = contents.trim().parse()?;
    Ok(num)
}


fn main() {
    for path in &["/dev/null", "/nowhere", "/tmp/this_file_contains_3"] {
	match open_and_parse_file(&path) {
	    Ok(n) => {
		println!(" File {} had {}", &path, n);
	    },
	    Err(e) => {
		println!(" File {} err {:?}", &path, e);
	    },
	};
    }
}

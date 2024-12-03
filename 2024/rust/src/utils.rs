// use std::fs::File;
// use std::io::{self, BufRead, BufReader};
use std::io;

/// Liest den Inhalt einer Datei zeilenweise in einen Vektor von Strings ein.
// pub fn read_lines<P>(filename: P) -> io::Result<Vec<String>>
// where
//     P: AsRef<std::path::Path>,
// {
//     let file = File::open(filename)?;
//     let reader = BufReader::new(file);
//     reader.lines().collect()
// }

/// Reads the entire content of a file into a String.
pub fn read_to_string<P>(filename: P) -> io::Result<String>
where
    P: AsRef<std::path::Path>,
{
    std::fs::read_to_string(filename)
}

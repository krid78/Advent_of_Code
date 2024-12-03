use crate::utils::read_to_string;

/// Reads the file and parses its content into a vector of vectors of integers.
fn prepare_data(filename: &str) -> Vec<Vec<i32>> {
    let input = match read_to_string(filename) {
        Ok(data) => data,
        Err(e) => {
            eprintln!("Error reading file: {}", e);
            return Vec::new();
        }
    };

    input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .filter_map(|num| num.parse::<i32>().ok()) // Parse each number, skip invalid ones
                .collect()
        })
        .collect()
}

/// Checks if a row is strictly monotonically increasing or decreasing
/// with a difference of at least 1 and at most 3 between adjacent numbers.
fn is_monotonic(row: &[i32]) -> bool {
    if row.len() < 2 {
        return false; // A single number or empty row cannot be monotonic
    }

    let mut increasing = true;
    let mut decreasing = true;

    for window in row.windows(2) {
        let diff = window[1] - window[0];
        if !(1 <= diff && diff <= 3) {
            increasing = false;
        }
        if !(-3 <= diff && diff <= -1) {
            decreasing = false;
        }
    }

    increasing || decreasing
}

/// Solves the task for Day 2.
pub fn solve() {
    let data = prepare_data("../data/day02.test");

    let mut solution: i32 = 0;

    // Check each row for monotonicity
    for (index, row) in data.iter().enumerate() {
        if is_monotonic(row) {
            println!("Row {} is monotonic: {:?}", index + 1, row);
            solution += 1;
        } else {
            println!("Row {} is not monotonic: {:?}", index + 1, row);
        }
    }
    println!("Number of monotonic rows: {:?}", solution);
}

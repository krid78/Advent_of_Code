use crate::utils::read_to_string; // Import the utility for reading file content
use std::collections::HashMap;   // Import HashMap for frequency counting

/// Prepares the data by reading from the file and returning sorted vectors for left and right columns.
fn prepare_data(filename: &str) -> (Vec<i32>, Vec<i32>) {
    // Read the data file
    let input = match read_to_string(filename) {
        Ok(data) => data,
        Err(e) => {
            eprintln!("Error reading file: {}", e);
            return (Vec::new(), Vec::new());
        }
    };

    // Parse the file content into two lists
    let mut left_column = Vec::new();
    let mut right_column = Vec::new();

    for line in input.lines() {
        // Split each line by whitespace
        let columns: Vec<&str> = line.split_whitespace().collect();

        if columns.len() == 2 {
            // Parse columns as integers and add to respective lists
            if let (Ok(left), Ok(right)) = (columns[0].parse::<i32>(), columns[1].parse::<i32>()) {
                left_column.push(left);
                right_column.push(right);
            } else {
                eprintln!("Skipping invalid line: {}", line);
            }
        } else {
            eprintln!("Skipping malformed line: {}", line);
        }
    }

    // Sort the columns
    left_column.sort();
    right_column.sort();

    (left_column, right_column)
}

/// Solves Part 1: Computes the sum of absolute differences between corresponding values.
pub fn solve_part1() {
    let (left_column, right_column) = prepare_data("../data/day01.data");

    let sum_of_differences: i32 = left_column
        .iter()
        .zip(right_column.iter())
        .map(|(left, right)| (left - right).abs())
        .sum();

    println!("Part 1 - Sum of absolute differences: {}", sum_of_differences);
}

/// Solves Part 2: Computes the weighted sum of frequencies.
pub fn solve_part2() {
    let (left_column, right_column) = prepare_data("../data/day01.data");

    // Compute the frequency of each number in right_column
    let mut frequency_map = HashMap::new();
    for &value in &right_column {
        *frequency_map.entry(value).or_insert(0) += 1;
    }

    let sum_of_frequencies: i32 = left_column
        .iter()
        .map(|&left_value| {
            let count = frequency_map.get(&left_value).cloned().unwrap_or(0);
            left_value * count
        })
        .sum();

    println!("Part 2 - Sum of frequencies: {}", sum_of_frequencies);
}

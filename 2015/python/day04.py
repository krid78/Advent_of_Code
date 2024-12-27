"""Solve Advent of Code 2015, day 4

https://adventofcode.com/2015/day/4
"""

import hashlib
import time


def solve_part1(the_data: str, pattern: str = "00000") -> int:
    """Solve the puzzle."""
    solution = 0

    while solution < 100_000_000:
        # Append the number to the base string
        candidate = f"{the_data}{solution}"

        # Compute the MD5 hash
        md5_hash = hashlib.md5(candidate.encode()).hexdigest()

        # Check if hash starts with the required number of zeros
        if md5_hash.startswith(pattern):
            return solution

        # Increment the number for the next attempt
        solution += 1

    return -1


def main(test=False):
    """Use main function to avoid global variables"""
    solution1 = solution2 = 0
    if test:
        the_data = "abcdef"  # get_data("2015/data/day04.test")
    else:
        the_data = "ckczppom"  # get_data("2015/data/day04.data")

    # Solve part 1
    time_start = time.perf_counter()
    solution1 = solve_part1(the_data, "00000")
    print(f"Part 1 ({solution1}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # solve part 2
    time_start = time.perf_counter()
    solution2 = solve_part1(the_data, "000000")
    print(f"Part 2 ({solution2}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # Finally
    print(f"{solution1=} | {solution2=}")


if __name__ == "__main__":
    main(test=False)

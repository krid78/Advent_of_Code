#!/usr/bin/env python3
"""Solve Advent of Code 2023/12/01
https://adventofcode.com/2023/day/1
"""

import string


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def main():
    """Solve day 01"""
    solution = 0
    # the_data = get_data("day01_test1.txt")
    the_data = get_data("day01_data.txt")

    for line in the_data:
        for letter in line:
            if letter in string.digits:
                left = letter
                break
        print(f"{line}: {left}")

        for letter in line[::-1]:
            if letter in string.digits:
                right = letter
                break
        print(f"{line}: {right}")

        print(f"{line}: {left}{right}")
        solution += int(f"{left}{right}")

    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

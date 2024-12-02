#!/usr/bin/env python3
"""Solve Advent of Code 2024/12/01
https://adventofcode.com/2024/day/1
"""
from collections import Counter


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def main():
    """Solve day 01"""

    solution1 = 0
    solution2 = 0
    # the_data = get_data("../../day01/test01.txt")
    the_data = get_data("../../day01/data01.txt")

    left = []
    right = []

    for line in the_data:
        lft, rght = tuple(line.split())
        left.append(int(lft.strip()))
        right.append(int(rght.strip()))

    left.sort()
    right.sort()

    assert len(left) == len(right)

    # Use zip for solution1
    for l, r in zip(left, right):
        solution1 += abs(l - r)

    # Precompute counts in right using Counter
    right_counts = Counter(right)

    # Use precomputed counts for solution2
    for l in left:
        solution2 += l * right_counts[l]

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1=}")
    print(f"{solution2=}")

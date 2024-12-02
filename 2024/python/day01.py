#!/usr/bin/env python3
"""Solve Advent of Code 2024/12/01
https://adventofcode.com/2024/day/1
"""


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

    for idx in range(len(left)):
        solution1 += abs(left[idx] - right[idx])
        solution2 += left[idx] * right.count(left[idx])

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1=}")
    print(f"{solution2=}")

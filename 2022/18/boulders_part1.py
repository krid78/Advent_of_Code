#!/usr/bin/env python3
""" Advent of Code 2022/12/18
https://adventofcode.com/2022/day/18
"""

from itertools import combinations


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [tuple(map(int, row.strip().split(","))) for row in in_file]

    return content


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    surface = 6 * len(the_data)
    print(f"{len(the_data)} cubes have a maximum of {surface} sides")

    for b1, b2 in combinations(the_data, 2):
        dist = sum(abs(s1 - s2) for s1, s2 in zip(b1, b2))
        if dist == 1:
            surface -= 2
            # print(f"{b1} and {b2} are neighbours, {surface=}")

    return surface


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

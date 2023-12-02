#!/usr/bin/env python3
"""Solve Advent of Code 2023/12/01
https://adventofcode.com/2021/day/1
"""

import string


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def get_hits(line: str) -> dict:
    """Return a number"""
    # print(f"Try: {line}")
    hits = {}
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for n, w in enumerate(words):
        idx = 0
        while True:
            try:
                idx = line.index(w, idx)
                hits[idx] = str(n)
                idx += 1
            except ValueError:
                break

    for d in string.digits:
        idx = 0
        while True:
            try:
                idx = line.index(d, idx)
                hits[idx] = d
                idx += 1
            except ValueError:
                break

    left = hits[min(hits.keys())]
    right = hits[max(hits.keys())]

    # print(f"{line=}\n{hits=}\n{left},{right}")

    return left, right


def main():
    """Solve day 01"""
    solution = 0
    # the_data = get_data("day01_test2.txt")
    the_data = get_data("day01_data.txt")

    for line in the_data:
        for lidx, letter in enumerate(line):
            if letter in string.digits:
                left = letter
                break
        # print(f"{line}[{lidx}]: {left}")

        for ridx, letter in enumerate(line[::-1]):
            if letter in string.digits:
                right = letter
                break
        # print(f"{line}[{ridx}]: {right}")

        lidx = lidx + 1 if lidx < len(line) else len(line)
        left, _ = get_hits(line[:lidx])

        # ridx = ridx if ridx > 0 else 0
        ridx = len(line) - (ridx + 1)
        _, right = get_hits(line[ridx:])

        print(f"{line}: {left}{right}")
        solution += int(f"{left}{right}")
        right, left = "", ""
        ridx, lidx = -1, -1

    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

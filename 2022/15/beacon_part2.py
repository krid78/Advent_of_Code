#!/usr/bin/env python3
""" Advent of Code 2022/12/15
https://adventofcode.com/2022/day/15

Die Manhattan-Distanz ist eine Metrik, in der die Distanz d zwischen zwei
Punkten A und B als die Summe der absoluten Differenzen ihrer Einzelkoordinaten
definiert wird. (https://de.wikipedia.org/wiki/Manhattan-Metrik)

This time no "brute force" filling of all diamonds. This will take too long.
Thus I will only look at the requested row and count the occupied positions
there.
"""
import re


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    for check_line in range(4_000_000):
        occupied = []
        for data in the_data:
            sx, sy, bx, by = map(int, re.findall("\-?\d+", data))
            md = abs(sx - bx) + abs(sy - by)
            if abs(check_line - sy) < md:
                start = sx - (md - abs(check_line - sy))
                end = sx + (md - abs(check_line - sy))
                occupied.append((min(start, end), max(start, end)))
                # print(f"{check_line=:3}: {sx=:4}, {sy=:4}, {bx=:4}, {by=:4} | {md=:4}")

        # smallest start first
        occupied.sort()
        # print(f"{check_line=:3}: {occupied=}")

        start, end = occupied[0]
        candidates = []
        for st, en in occupied[1:]:
            if st <= end:
                end = max(end, en)
            else:
                candidates.append((start, end))
                start = st
                end = en
        if (start, end) not in candidates:
            candidates.append((start, end))

        if len(candidates) > 1:
            candidates.sort()
            # print(f"{check_line=:3}: {occupied=}")
            print(f"{check_line=:3}: {candidates=}")
        if len(candidates) == 2:
            print(f"{(candidates[0][1]+1) * 4_000_000 + check_line} ")

    return candidates[0][1] + 1 * 4_000_000 + check_line


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

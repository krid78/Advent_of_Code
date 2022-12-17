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

# __TARGET_LINE__ = 10
__TARGET_LINE__ = 2_000_000


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

    occupied = []
    b_in_line = set()

    for data in the_data:
        sx, sy, bx, by = map(int, re.findall("\-?\d+", data))
        assert sx >= 0
        assert sy >= 0
        md = abs(sx - bx) + abs(sy - by)
        if abs(sy - __TARGET_LINE__) < md:
            start = sx - (md - abs(__TARGET_LINE__ - sy))
            end = sx + (md - abs(__TARGET_LINE__ - sy))
            occupied.append((start, end))
            print(f"{sx=:7}, {sy=:7}, {bx=:7}, {by=:7} | {md=:7}")
        if by == __TARGET_LINE__:
            b_in_line.add((bx, by))

    print(f"{occupied=}, {len(b_in_line)}")

    st, en = occupied[0]
    for st, en in occupied:
        start = min(start, st)
        end = max(end, en)
    print(f"{end} - {start} == {end - start}")

    return end - start


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

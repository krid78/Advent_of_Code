#!/usr/bin/env python3
"""Solve Advent of Code 2023/12/03
https://adventofcode.com/2023/day/3
"""

import string


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def main():
    """Solve day 02"""
    solution = 0
    # the_data = get_data("day03_test1.txt")
    the_data = get_data("day03_data.txt")

    line_len = len(the_data[0])

    numbers = []
    signs = []

    for row, line in enumerate(the_data):
        # new row
        in_number = False
        number = ""
        for col, val in enumerate(line):
            if val in string.digits:
                # found a number
                if not in_number:
                    in_number = True
                    number = val
                    start = (row, col)
                else:
                    number += val
            else:
                if col == (line_len - 1):
                    stop = (row, col)
                else:
                    stop = (row, col - 1)

                if ord(val) != 46:
                    # found a special sign
                    signs.append((row, col))

                if in_number:
                    numbers.append(
                        {
                            "start": start,
                            "stop": stop,
                            "val": int(number),
                            "valid": False,
                        }
                    )
                    in_number = False
                    number = ""
                    start = None
                    stop = None

    for number in numbers:
        # search for signs around the number
        # in row-1 from start_col - 1 .. start_col + 1
        # in row+0 from start_col - 1 .. start_col + 1
        # in row+1 from start_col - 1 .. start_col + 1
        tl = [number["start"][0] - 1, number["start"][1] - 1]
        if tl[0] < 0:
            tl[0] = 0
        if tl[1] < 0:
            tl[1] = 0
        tl = tuple(tl)

        br = [number["stop"][0] + 1, number["stop"][1] + 1]
        if br[0] >= (len(the_data) - 1):
            br[0] = len(the_data) - 1
        if br[1] >= (line_len - 1):
            br[1] = line_len - 1
        br = tuple(br)

        for row in range(tl[0], br[0] + 1):
            for col in range(tl[1], br[1] + 1):
                if (row, col) in signs:
                    number["valid"] = True
                    break

    for number in numbers:
        if number["valid"] is True:
            solution += number["val"]

    return solution


if __name__ == "__main__":
    solution = main()
    print(f"solution = {solution}")

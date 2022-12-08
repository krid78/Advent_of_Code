#!/usr/bin/env python3
""" Advent of Code 2022/12/08
https://adventofcode.com/2022/day/8
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def main():
    the_data = get_data("data_test.txt")
    # the_data = get_data("data.txt")

    # outside trees
    total = len(the_data[0]) + len(the_data[-1]) + 2 * (len(the_data) - 2)

    for ridx in range(1, len(the_data) - 1):
        row = the_data[ridx]
        print(f"{row=}")
        for cidx in range(1, len(row) - 1):
            col = [vtree[cidx] for vtree in the_data]
            if max(row[:cidx]) < row[cidx] or max(row[cidx + 1 :]) < row[cidx] or max(col[:ridx]) < row[cidx] or max(col[ridx + 1 :]) < row[cidx]:
                total += 1

    print(f"{total=}")


if __name__ == "__main__":
    main()

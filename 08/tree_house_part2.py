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


def view_distance(height, field):
    """search for the idx of a value in a list"""
    # print(f"Search {height} in {field}")

    for idx in range(len(field)):
        if field[idx] >= height:
            break

    return idx + 1


def main():
    # the_data = get_data("data_test.txt")
    the_data = get_data("data.txt")

    # view scores
    total = []

    # view scores for all edge trees is zero
    for ridx in range(1, len(the_data) - 1):
        row = the_data[ridx]
        for cidx in range(1, len(row) - 1):
            col = "".join([vtree[cidx] for vtree in the_data])
            print(f"{row=} : {row[:cidx]}{row[cidx+1:]}")
            total.append(
                view_distance(row[cidx], row[:cidx][::-1])
                * view_distance(row[cidx], row[cidx + 1 :])
                * view_distance(row[cidx], col[:ridx][::-1])
                * view_distance(row[cidx], col[ridx + 1 :])
            )

    total.sort()
    print(f"{total=}")


if __name__ == "__main__":
    main()

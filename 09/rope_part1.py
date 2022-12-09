#!/usr/bin/env python3
""" Advent of Code 2022/12/09
https://adventofcode.com/2022/day/9
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def main():
    """code if module is called directly"""
    the_data = get_data("data_test.txt")
    # the_data = get_data("data.txt")

    total = 0
    directions = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
    total = set()
    hx = 0
    hy = 0
    tx = 0
    ty = 0

    for move in the_data:
        print(f"{move=}")
        direction, steps = move.split()
        for _ in range(int(steps)):
            # move Head
            hx += directions[direction][0]
            hy += directions[direction][1]
            # move tail, if distance is > 1
            if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                tx = hx - directions[direction][0]
                ty = hy - directions[direction][1]

            total.add((tx, ty))
            print(f"Head: {hx}, {hy} and Tail: {tx}, {ty}; Uniques: {len(total)}")

    print(f"Fields of the Tail: {len(total)}")


if __name__ == "__main__":
    main()

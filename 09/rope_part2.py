#!/usr/bin/env python3
""" Advent of Code 2022/12/09
https://adventofcode.com/2022/day/9

Solution: 2562
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
    # the_data = get_data("data_test1.txt")
    # the_data = get_data("data_test2.txt")
    the_data = get_data("data.txt")

    total = 0
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    total = set()
    knots = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    ]

    for move in the_data:
        print(f"{move=}")
        direction, steps = move.split()
        for _ in range(int(steps)):
            # move Head
            dx, dy = directions[direction]
            knots[0][0] += dx
            knots[0][1] += dy

            for idx in range(1, len(knots)):
                dx = knots[idx - 1][0] - knots[idx][0]
                dy = knots[idx - 1][1] - knots[idx][1]
                if abs(dx) >= 2 and dy == 0:
                    knots[idx][0] += dx // abs(dx)
                elif abs(dy) >= 2 and dx == 0:
                    knots[idx][1] += dy // abs(dy)
                elif abs(dx) + abs(dy) >= 3:
                    knots[idx][0] += dx // abs(dx)
                    knots[idx][1] += dy // abs(dy)

            total.add((knots[9][0], knots[9][1]))

            print(
                f"Head: {knots[0][0]}, {knots[0][1]} and Tail: {knots[9][0]},"
                f"{knots[9][1]}; Uniques: {len(total)}"
            )

    print(f"Fields of the Tail: {len(total)}")


if __name__ == "__main__":
    main()

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
    # the_data = get_data("data_test1.txt")
    # the_data = get_data("data_test2.txt")
    the_data = get_data("data.txt")

    total = 0
    directions = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
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
            dirx, diry = directions[direction]
            knots[0][0] += dirx
            knots[0][1] += diry
            for idx in range(1, len(knots)):
                dx = knots[idx - 1][0] - knots[idx][0]
                dy = knots[idx - 1][1] - knots[idx][1]
                """
                if move in x and delta in x == 2 and delta in y == 1; move in x and y
                if move in x and delta in x == 2; move in x
                if move in x and delta in y == 2; move in y
                if move in y and delta in x == 1 and delta in y == 2; move in x and y
                if move in y and delta in y == 2; move in y
                if move in y and delta in x == 2; move in x
                """
                if (abs(dirx) == 1 and abs(dx) == 2 and abs(dy) == 1) or (
                    abs(diry) == 1 and abs(dy) == 2 and abs(dx) == 1
                ):
                    knots[idx][0] = knots[idx - 1][0] - dirx
                    knots[idx][1] = knots[idx - 1][1] - diry
                elif abs(dirx) == 1 and abs(dx) == 2 and abs(dy) == 0:
                    if dx != 0:
                        knots[idx][0] += dx // abs(dx)
                elif abs(diry) == 1 and abs(dy) == 2 and abs(dx) == 0:
                    if dy != 0:
                        knots[idx][1] += dy // abs(dy)
                elif abs(dirx) == 1 and abs(dy) == 2:
                    if dx != 0:
                        knots[idx][0] += dx // abs(dx)
                    if dy != 0:
                        knots[idx][1] += dy // abs(dy)
                elif abs(diry) == 1 and abs(dx) == 2:
                    if dx != 0:
                        knots[idx][0] += dx // abs(dx)
                    if dy != 0:
                        knots[idx][1] += dy // abs(dy)
                else:
                    break

            total.add((knots[9][0], knots[9][1]))
            print(
                f"Head: {knots[0][0]}, {knots[0][1]} and Tail: {knots[9][0]},"
                f"{knots[9][1]}; Uniques: {len(total)}"
            )

    print(f"Fields of the Tail: {len(total)}")


if __name__ == "__main__":
    main()

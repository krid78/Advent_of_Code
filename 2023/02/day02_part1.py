#!/usr/bin/env python3
"""Solve Advent of Code 2023/12/02
https://adventofcode.com/2021/day/2
"""


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def main():
    """Solve day 02"""
    solution = 0
    # the_data = get_data("day02_test1.txt")
    the_data = get_data("day02_data.txt")

    red = 12
    green = 13
    blue = 14

    for line in the_data:
        game, cube_sets = tuple(line.split(": "))
        cube_sets = cube_sets.split(";")
        game = game.strip().split()
        colors = {}
        impossible = 0

        print(f"{cube_sets}")

        for cs in cube_sets:
            cs = cs.strip().replace(",", "").split()
            # print(f"{cs=}")

            for idx in range(1, len(cs), 2):
                colors[cs[idx]] = 0
                colors[cs[idx]] = int(cs[idx - 1])

            print(f" - {colors=}")

            if (
                "red" in colors.keys()
                and colors["red"] > red
                or "green" in colors.keys()
                and colors["green"] > green
                or "blue" in colors.keys()
                and colors["blue"] > blue
            ):
                print(f"{game} is impossible")
                impossible = 1

        if not impossible:
            print(f"{game}")
            solution += int(game[1])

    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

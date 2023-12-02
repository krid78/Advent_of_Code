#!/usr/bin/env python3
"""Solve Advent of Code 2023/12/01
https://adventofcode.com/2021/day/1
"""


from multiprocessing import Value


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

    for line in the_data:
        game, cube_sets = tuple(line.split(": "))
        cube_sets = cube_sets.split(";")
        game = game.strip().split()
        colors = {}

        print(f"{cube_sets}")

        for cs in cube_sets:
            cs = cs.strip().replace(",", "").split()
            # print(f"{cs=}")

            for idx in range(1, len(cs), 2):
                if cs[idx] not in colors.keys():
                    colors[cs[idx]] = 0
                colors[cs[idx]] = max(colors[cs[idx]], int(cs[idx - 1]))

        print(f" - {colors=}")

        power = 1
        for _, v in colors.items():
            power *= v

        solution += power

    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

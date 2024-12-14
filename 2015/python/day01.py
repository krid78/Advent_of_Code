"""Solve Advent of Code 2015, day 1

https://adventofcode.com/2015/day/1
"""

import time


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content[0]


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2015/data/day01.data")
    # the_data = get_data("2015/data/day01.test")

    for idx, direction in enumerate(the_data):
        if direction == "(":
            solution1 += 1
        else:
            solution1 -= 1

        if solution1 < 0 and solution2 == 0:
            solution2 = idx + 1

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

"""Solve Advent of Code 2024, day 8

https://adventofcode.com/2024/day/8
"""

import time
from itertools import combinations


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def draw_board(the_data: list[str], antinodes: set[tuple[int, int]]):
    """Draw the board to check the result"""
    lrow = len(the_data)
    lcol = len(the_data[0])
    print("=" * (lcol // 2) + f"{lrow}x{lcol}" + "=" * (lcol // 2))
    for row in range(lrow):
        for col in range(lcol):
            if (row, col) in antinodes:
                print("#", end="")
            else:
                print(the_data[row][col], end="")
        print("")


def find_antinodes(antennas, lrow, lcol):
    """Find the antinodes"""
    antinodes = set()

    for key, value in antennas.items():
        print(f"{key=}, {value=}")
        for (row1, col1), (row2, col2) in combinations(value, 2):
            dr = row2 - row1
            dc = col2 - col1
            if 0 <= row1 - dr < lrow and 0 <= col1 - dc < lcol:
                antinodes.add((row1 - dr, col1 - dc))
            if 0 <= row2 + dr < lrow and 0 <= col2 + dc < lcol:
                antinodes.add((row2 + dr, col2 + dc))

    return antinodes


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day08.data")
    # the_data = get_data("2024/data/day08.test")

    antennas = {}

    lrow = len(the_data)
    lcol = len(the_data[0])
    for row in range(lrow):
        for col in range(lcol):
            if the_data[row][col] != ".":
                antennas.setdefault(the_data[row][col], set()).add((row, col))

    antinodes = find_antinodes(antennas, lrow, lcol)
    solution1 = len(antinodes)

    draw_board(the_data, antinodes)

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

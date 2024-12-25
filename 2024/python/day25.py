"""Solve Advent of Code 2024, day 25

https://adventofcode.com/2024/day/25
"""

import time


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def digitalize_schematic(schematic: list[str], reverse=False) -> list[int]:
    form = []
    if reverse:
        start = 4
        stop = -1
        step = -1
    else:
        start = 0
        stop = 5
        step = 1
    for col in range(5):
        height = 0
        for row in range(start, stop, step):
            if schematic[row][col] == "#":
                height += 1
        form.append(height)
    return form


def parse_data_cool(
    the_data: list[str],
) -> tuple[list[tuple[int, int, int, int, int]], list[tuple[int, int, int, int, int]]]:
    """Split the data into digitalized locks and keys"""
    locks = []
    keys = []

    idx = row = 0
    last_schema = False
    while not last_schema:
        try:
            idx = the_data.index("", row)
        except ValueError:
            idx = len(the_data)
            last_schema = True
        print(the_data[row:idx])
        if the_data[row] == "#####":
            locks.append(digitalize_schematic(the_data[row + 1 : idx - 1]))
        else:
            keys.append(digitalize_schematic(the_data[row + 1 : idx - 1], True))
        row = idx + 1
    return locks, keys


def parse_data(
    the_data: list[str],
) -> tuple[list[tuple[int, int, int, int, int]], list[tuple[int, int, int, int, int]]]:
    """Split the data into digitalized locks and keys"""
    locks = []
    keys = []

    gap = row = 0
    last_schema = False
    while not last_schema:
        try:
            idx = the_data.index("", row)
            gap = the_data[row:].index("")
        except ValueError:
            idx = len(the_data)
            gap = len(the_data) - row
            last_schema = True
        # print(the_data[row : row + gap])
        # print(the_data[row:idx])
        if the_data[row] == "#####":
            # lock
            locks.append(digitalize_schematic(the_data[row + 1 : row + gap - 1]))
        else:
            keys.append(digitalize_schematic(the_data[row + 1 : row + gap - 1], True))
        row += gap + 1
    return locks, keys


def solve_part1(the_data: list[str]) -> int:
    """Solve the puzzle."""
    solution = 0

    locks, keys = parse_data(the_data)

    for l0, l1, l2, l3, l4 in locks:
        for k0, k1, k2, k3, k4 in keys:
            # print(f"Match {[k0, k1, k2, k3, k4]} to {[l0, l1, l2, l3, l4]}")
            if k0 + l0 > 5 or k1 + l1 > 5 or k2 + l2 > 5 or k3 + l3 > 5 or k4 + l4 > 5:
                print(
                    f"No match for key {[k0, k1, k2, k3, k4]} to lock {[l0, l1, l2, l3, l4]}"
                )
            else:
                solution += 1

    return solution


def solve_part2(the_data: list[str]) -> int:
    """Solve the puzzle."""
    solution = 0

    return solution


if __name__ == "__main__":
    __the_data__ = get_data("2024/data/day25.data")
    # __the_data__ = get_data("2024/data/day25.test")

    # Solve part 1
    time_start = time.perf_counter()
    solution1 = solve_part1(__the_data__)
    print(f"Part 1 ({solution1}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # solve part 1
    time_start = time.perf_counter()
    solution2 = solve_part2(__the_data__)
    print(f"Part 2 ({solution2}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # Finally
    print(f"{solution1=} | {solution2=}")

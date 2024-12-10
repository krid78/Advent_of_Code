"""Solve Advent of Code 2024, day 10

https://adventofcode.com/2024/day/10
"""

import time

__DIRECTIONS__ = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # North  # East  # South  # West


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        # content = [row.rstrip() for row in in_file]
        content = [list(map(int, line.strip())) for line in in_file]

    return content


def get_mapdata(mapdata, x, y):
    if 0 <= x < len(mapdata[0]) and 0 <= y < len(mapdata):
        return mapdata[y][x]
    else:
        return -1


def walk(data, cur_x, cur_y, cur_val):
    if cur_val == 0:
        return [(cur_x, cur_y)]

    zeros = []
    for dx, dy in __DIRECTIONS__:
        next_x = cur_x + dx
        next_y = cur_y + dy
        next_val = get_mapdata(data, next_x, next_y)
        if next_val == (cur_val - 1):
            zeros.extend(walk(data, next_x, next_y, next_val))

    return zeros


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day10.data")
    # the_data = get_data("2024/data/day10.test")
    # the_data = [[0, 1, 2, 3], [1, 2, 3, 4], [8, 7, 6, 5], [9, 8, 7, 6]]

    max_x = len(the_data[0])
    max_y = len(the_data)
    zeros = set(
        [(x, y) for y in range(max_y) for x in range(max_x) if the_data[y][x] == 0]
    )
    nines = set(
        [(x, y) for y in range(max_y) for x in range(max_x) if the_data[y][x] == 9]
    )
    paths1 = []
    paths2 = []

    for x, y in nines:
        paths = walk(the_data, x, y, 9)
        paths2.extend(paths)
        paths1.extend(set(paths))

    solution1 = sum([paths1.count((x, y)) for x, y in zeros])
    solution2 = sum([paths2.count((x, y)) for x, y in zeros])

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

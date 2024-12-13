"""Solve Advent of Code 2024, day 12

https://adventofcode.com/2024/day/12
"""

import time
from collections import defaultdict

__DIRECTIONS__ = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        return [row.rstrip() for row in in_file]


def calc_perimeter(area: set[tuple[int, int]]) -> int:
    """Calculate the perimeter of an area."""
    perimeter = 0
    for row, col in area:
        for dr, dc in __DIRECTIONS__:
            if (row + dr, col + dc) not in area:
                perimeter += 1
    return perimeter


def count_corners(area: set[tuple[int, int]]) -> int:
    """Count the corner points of a given area."""
    diagonal = [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)]
    candidates = defaultdict(int)

    for row, col in area:
        for dr, dc in diagonal:
            candidates[(row + dr, col + dc)] += 1

    return sum(1 for count in candidates.values() if count % 2 != 0)


def add_plot(
    the_data: list[str], unvisited: set[tuple[int, int]], row: int, col: int, plant: str
) -> set[tuple[int, int]]:
    """Collect all plots in the same area."""
    stack = [(row, col)]
    area = set()

    while stack:
        r, c = stack.pop()
        if (r, c) in unvisited:
            unvisited.remove((r, c))
            area.add((r, c))
            for dr, dc in __DIRECTIONS__:
                nr, nc = r + dr, c + dc
                if (nr, nc) in unvisited and the_data[nr][nc] == plant:
                    stack.append((nr, nc))

    return area


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day12.data")
    # the_data = get_data("2024/data/day12.test")
    unvisited = {
        (row, col) for row in range(len(the_data)) for col in range(len(the_data[0]))
    }

    areas = []
    while unvisited:
        row, col = min(unvisited)
        areas.append(add_plot(the_data, unvisited, row, col, the_data[row][col]))

    for a in areas:
        solution1 += calc_perimeter(a) * len(a)
        solution2 += count_corners(a) * len(a)

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

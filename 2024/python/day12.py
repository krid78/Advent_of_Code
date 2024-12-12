"""Solve Advent of Code 2024, day 12

https://adventofcode.com/2024/day/12
"""

import time

__DIRECTIONS__ = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def get_plant(the_data, plot, plant):
    """check if position is still valid"""
    if (
        0 <= plot[0] < len(the_data)
        and 0 <= plot[1] < len(the_data[0])
        and the_data[plot[0]][plot[1]] == plant
    ):
        return True
    return False


def calc_perimeter(area):
    perimeter = 0
    for plot in area:
        row, col = plot
        peri = 4
        for dr, dc in __DIRECTIONS__:
            if (row + dr, col + dc) in area:
                peri -= 1
        perimeter += peri
    return perimeter


def count_sides(area):
    if len(area) == 1:
        return 4

    area.sort()
    sides = 1
    start = area[0]
    r, c = start
    d = 1  # starting direction
    dr, dc = __DIRECTIONS__[d]
    turns = 0

    while True:
        nr, nc = r + dr, c + dc
        if (nr, nc) == start:
            break
        elif (nr, nc) in area:
            if turns != 0:
                sides += 2 - (turns % 2)
                turns = 0
        else:
            for turn in (1, -1, 2):
                nd = (d + turn) % 4
                dr, dc = __DIRECTIONS__[nd]
                if (r + dr, c + dc) in area:
                    d = nd
                    turns = abs(turn)
                    break
            continue

        r, c = nr, nc

    if d != 0:
        sides += 1

    return sides


def add_plot(the_data, unvisited, row, col, plant):
    """check current garden plot"""
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

    # the_data = get_data("2024/data/day12.data")
    the_data = get_data("2024/data/day12.test")
    unvisited = {
        (row, col) for row in range(len(the_data)) for col in range(len(the_data[0]))
    }

    areas = []
    while unvisited:
        row, col = next(iter(unvisited))
        areas.append(add_plot(the_data, unvisited, row, col, the_data[row][col]))

        a = areas[-1]
        p = calc_perimeter(list(a))
        s = count_sides(list(a))
        print(f"== Area: {the_data[row][col]} ==")
        print(f"Area size: {len(a)}")
        print(f"Perimeter: {p}")
        print(f"Sides    : {s}")
        print(f"Cost1: {len(a)*p}")
        print(f"Cost2: {len(a)*s}")
        print(f"{a=}\n")

    for a in areas:
        solution1 += calc_perimeter(list(a)) * len(a)
        solution2 += count_sides(list(a)) * len(a)

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

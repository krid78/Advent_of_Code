"""Solve Advent of Code 2024, day 6

https://adventofcode.com/2024/day/6
"""

import time

__DIRECTIONS__ = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
]


def get_data(filename: str) -> list[str]:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def solve_part2(
    the_data: list[str], obstructions: list[set], start: set[int], direction: int
) -> int:
    """Solve part 2"""

    row, col = start
    dr, dc = __DIRECTIONS__[direction]
    visited = [start]
    counter = 0

    while (
        0 < row < len(the_data) - 1 and 0 < col < len(the_data[0]) - 1 and counter < 150
    ):
        row += dr
        col += dc
        if (row, col) in obstructions:
            row -= dr
            col -= dc
            direction = (direction + 1) % 4
            dr, dc = __DIRECTIONS__[direction]
        elif (row, col) not in visited:
            the_data[row] = the_data[row][:col] + "X" + the_data[row][col + 1 :]
            visited.append((row, col))
            counter = 0
        else:
            counter += 1

    if counter >= 150:
        return True
    else:
        return False


def solve_part1(the_data: list[str], obstructions, start, direction) -> int:
    """Solve part 1"""

    row, col = start
    dr, dc = __DIRECTIONS__[direction]
    visited = [start]

    while 0 < row < len(the_data) - 1 and 0 < col < len(the_data[0]) - 1:
        row += dr
        col += dc
        if (row, col) in obstructions:
            row -= dr
            col -= dc
            direction = (direction + 1) % 4
            dr, dc = __DIRECTIONS__[direction]
        elif (row, col) not in visited:
            the_data[row] = the_data[row][:col] + "X" + the_data[row][col + 1 :]
            visited.append((row, col))
        else:
            pass

    # print("\n".join(the_data))

    return visited, len(visited)


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day06.data")
    # the_data = get_data("2024/data/day06.test")

    obstructions = []

    for row, rdata in enumerate(the_data):
        for col, cdata in enumerate(rdata):
            if cdata == "#":
                obstructions.append((row, col))
            elif cdata == "^":
                direction = 0
                start = (row, col)
            elif cdata == ">":
                direction = 1
                start = (row, col)
            elif cdata == "v":
                direction = 2
                start = (row, col)
            elif cdata == "<":
                direction = 3
                start = (row, col)
            else:
                pass

    # print(f"{start=}, {obstructions=}")

    route, solution1 = solve_part1(the_data, obstructions, start, direction)
    length = len(route)
    for block in route[1:]:
        print(f"{length} left")
        if solve_part2(the_data, obstructions + [block], start, direction):
            solution2 += 1
        length -= 1

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

"""Solve Advent of Code 2024, day 10

https://adventofcode.com/2024/day/10
"""

import time

__DIRECTIONS__ = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # North, East, South, West


def get_data(filename: str) -> list[list[int]]:
    """
    Return file contents as a 2D list of integers.

    Args:
        filename (str): Path to the input file.

    Returns:
        list[list[int]]: The grid as a 2D list of integers.
    """
    with open(filename, "r") as in_file:
        return [list(map(int, line.strip())) for line in in_file]


def get_mapdata(mapdata: list[list[int]], x: int, y: int) -> int:
    """
    Get the value of a cell in the grid, returning -1 if out of bounds.

    Args:
        mapdata (list[list[int]]): The grid.
        x (int): X-coordinate.
        y (int): Y-coordinate.

    Returns:
        int: The value of the cell or -1 if out of bounds.
    """
    if 0 <= x < len(mapdata[0]) and 0 <= y < len(mapdata):
        return mapdata[y][x]
    return -1


def walk(
    data: list[list[int]], cur_x: int, cur_y: int, cur_val: int, visited: set
) -> list[tuple[int, int]]:
    """
    Recursively find all paths from a starting cell to any cell with value 0.

    Args:
        data (list[list[int]]): The grid.
        cur_x (int): Current X-coordinate.
        cur_y (int): Current Y-coordinate.
        cur_val (int): Current cell value.
        visited (set): Set of visited cells to prevent loops.

    Returns:
        list[tuple[int, int]]: A list of all positions with value 0 reachable from the start.
    """
    if cur_val == 0:
        return [(cur_x, cur_y)]

    zeros = []
    visited.add((cur_x, cur_y))
    for dx, dy in __DIRECTIONS__:
        next_x, next_y = cur_x + dx, cur_y + dy
        if (next_x, next_y) not in visited:
            next_val = get_mapdata(data, next_x, next_y)
            if next_val == cur_val - 1:
                zeros.extend(walk(data, next_x, next_y, next_val, visited))
    visited.remove((cur_x, cur_y))
    return zeros


def solve() -> tuple[int, int]:
    """
    Solve the puzzle for both parts.

    Returns:
        tuple[int, int]: The solutions for part 1 and part 2.
    """
    the_data = get_data("2024/data/day10.data")
    # the_data = get_data("2024/data/day10.test")

    max_x, max_y = len(the_data[0]), len(the_data)
    zeros = [(x, y) for y in range(max_y) for x in range(max_x) if the_data[y][x] == 0]
    nines = [(x, y) for y in range(max_y) for x in range(max_x) if the_data[y][x] == 9]

    # Count occurrences of zeros in all paths
    paths1_counts = {zero: 0 for zero in zeros}
    paths2_counts = {zero: 0 for zero in zeros}

    for x, y in nines:
        visited = set()
        paths = walk(the_data, x, y, 9, visited)
        for zero in set(paths):  # Unique paths for part 1
            paths1_counts[zero] += 1
        for zero in paths:  # All paths for part 2
            paths2_counts[zero] += 1

    solution1 = sum(paths1_counts.values())
    solution2 = sum(paths2_counts.values())

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

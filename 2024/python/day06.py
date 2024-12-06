"""Solve Advent of Code 2024, day 6

https://adventofcode.com/2024/day/6
"""

import time

# Directions: up, right, down, left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_data(filename: str) -> list[str]:
    """Return file contents as a list of strings."""
    with open(filename, "r") as in_file:
        return [row.rstrip() for row in in_file]


def parse_map(the_data: list[str]):
    """Parse the map and extract start position, direction, and obstructions."""
    obstructions = set()
    start = None
    direction = 0

    for row, line in enumerate(the_data):
        for col, char in enumerate(line):
            if char == "#":
                obstructions.add((row, col))
            elif char in "^>v<":
                start = (row, col)
                direction = "^>v<".index(char)

    return obstructions, start, direction


def traverse_map(
    the_data: list[str], obstructions: set, start: tuple, direction: int, max_steps=150
):
    """Simulate traversal of the map."""
    row, col = start
    dr, dc = DIRECTIONS[direction]
    visited = set()
    steps = 0

    while 0 < row < len(the_data) - 1 and 0 < col < len(the_data[0]) - 1:
        if steps >= max_steps:
            return False, visited

        row += dr
        col += dc

        if (row, col) in obstructions:
            # Hit an obstruction, turn clockwise
            row -= dr
            col -= dc
            direction = (direction + 1) % 4
            dr, dc = DIRECTIONS[direction]
        elif (row, col) not in visited:
            # Visit a new cell
            visited.add((row, col))
            steps = 0
        else:
            # Already visited
            steps += 1

    return True, visited


def solve():
    """Solve the puzzle."""
    the_data = get_data("2024/data/day06.data")
    obstructions, start, direction = parse_map(the_data)

    # Part 1: Traverse the map and count visited cells
    _, visited = traverse_map(the_data, obstructions, start, direction)
    solution1 = len(visited)

    # Part 2: Check blockages
    solution2 = 0
    for block in visited:
        new_obstructions = obstructions | {block}
        success, _ = traverse_map(the_data, new_obstructions, start, direction)
        if not success:
            solution2 += 1

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} seconds.")
    print(f"{solution1=} | {solution2=}")

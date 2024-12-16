"""Solve Advent of Code 2024, day 16

https://adventofcode.com/2024/day/16
"""

import time

__DIRECTIONS__ = [(-1, 0), (0, 1), (1, 0), (-1, 0)]


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def parse_data(content: list[str]) -> tuple[set[tuple], set[tuple], tuple, tuple]:
    rows = len(content)
    cols = len(content[0])
    floors = set()
    walls = set()

    for r in range(rows):
        for c in range(cols):
            if content[r][c] in ".SE":
                floors.add((r, c))
                if content[r][c] == "S":
                    start = (r, c)
                elif content[r][c] == "E":
                    goal = (r, c)
            elif content[r][c] == "#":
                walls.add((r, c))
            else:
                raise (ValueError)

    return walls, floors, start, goal


def solve_part1(
    walls, unvisited_floors: set, position: tuple, direction: int, goal: tuple
) -> tuple[int, bool]:
    """Find a way from position to goal.

    turn 90 degrees (cost 1000) or move 1 step into current direction (cost 1)

    Args:
        walls (set): walls in the map
        unvisited_floors (set): not yet visited floors
        position (tuple): _description_
        goal (tuple): _description_
    """
    costs = []
    success = False
    if position == goal:
        return 0, True

    (r, c) = position

    unvisited_floors.remove((r, c))
    for turn in [0, 1, -1]:
        new_dir = (direction + turn) % 4
        dr, dc = __DIRECTIONS__[new_dir]
        nr, nc = r + dr, c + dc
        if (nr, nc) in unvisited_floors:
            cost, success = solve_part1(
                walls, unvisited_floors, (nr, nc), new_dir, goal
            )
            if success:
                costs.append(cost + 1 + (999 * abs(turn)))

    unvisited_floors.add((r, c))

    if costs:
        return min(costs), True

    return None, False


def solve_part2():
    """Task unknown, until  part 1 is solved"""
    return 42


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    # the_data = get_data("2024/data/day16.data")
    the_data = get_data("2024/data/day16.1.test")
    walls, floors, start, goal = parse_data(the_data)

    solution1 = solve_part1(walls, floors, start, 1, goal)
    solution2 = solve_part2()

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

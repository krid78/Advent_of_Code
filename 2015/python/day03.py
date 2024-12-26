"""Solve Advent of Code 2015, day 3

https://adventofcode.com/2015/day/3
"""

import time

__DIRECTION_MAP__ = {
    "^": (-1, 0),  # North
    ">": (0, 1),  # East
    "v": (1, 0),  # South
    "<": (0, -1),  # West
}


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def move(moves: str) -> set[tuple[int, int]]:
    position_r = 0
    position_c = 0
    visited = {(position_r, position_c)}
    revisited = 0
    for move in moves:
        position_r += __DIRECTION_MAP__[move][0]
        position_c += __DIRECTION_MAP__[move][1]
        if (position_r, position_c) not in visited:
            visited.add((position_r, position_c))
        else:
            revisited += 1

    return visited


def solve_part1(the_data: list[str], row: int = 0) -> int:
    """Solve the puzzle."""

    moves = the_data[row]

    visited = move(moves)

    return len(visited)


def solve_part2(the_data: list[str], row: int = 0) -> int:
    """Solve the puzzle."""
    moves = the_data[row]
    smoves = "".join([moves[m] for m in range(0, len(moves), 2)])
    rmoves = "".join([moves[m] for m in range(1, len(moves), 2)])
    rmoves = rmoves

    print(f"{moves=}")
    print(f"{smoves=}")
    print(f"{rmoves=}")

    svisited = move(smoves)
    rvisited = move(rmoves)

    together = svisited | rvisited

    return len(together)


def main(test=False):
    """Use main function to avoid global variables"""
    if test:
        the_data = get_data("2015/data/day03.test")
    else:
        the_data = get_data("2015/data/day03.data")

    # Solve part 1
    time_start = time.perf_counter()
    solution1 = solve_part1(the_data, 0)
    print(f"Part 1 ({solution1}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # solve part 1
    time_start = time.perf_counter()
    solution2 = solve_part2(the_data, 0)
    print(f"Part 2 ({solution2}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # Finally
    print(f"{solution1=} | {solution2=}")


if __name__ == "__main__":
    # main(test=True)
    main(test=False)

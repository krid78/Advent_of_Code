"""Solve Advent of Code 2024, day 14

https://adventofcode.com/2024/day/14
"""

import time
from collections import deque


def get_data(filename: str) -> list[dict[str, tuple[int, int]]]:
    """
    Return file contents as a structured list of dictionaries.

    Args:
        filename (str): Path to the input file.

    Returns:
        list[dict[str, tuple[int, int]]]: A list of dictionaries, where each dictionary
        contains the position 'p' and velocity 'v' as tuples.
    """
    data = []
    with open(filename, "r") as in_file:
        for line in in_file:
            line = line.strip()
            if line:
                # Parse position (p) and velocity (v)
                p_part, v_part = line.split(" ")
                px, py = map(int, p_part[2:].split(","))
                vx, vy = map(int, v_part[2:].split(","))
                data.append({"p": (px, py), "v": (vx, vy)})
    return data


def draw_bot_map(bot_pos, max_row, max_col):
    for r in range(max_row):
        for c in range(max_col):
            if (r, c) in bot_pos:
                print(f"{bot_pos.count((r, c))}", end="")
            else:
                print(".", end="")
        print("")


def solve_part1(the_data, steps, max_row, max_col):
    quadrants = [0, 0, 0, 0]
    print(f"Quadrants:")
    print(f"  Rows: 0 <= r < {(max_row // 2)} and {(max_row // 2)} < r < {max_row}")
    print(f"  Cols: 0 <= c < {(max_col // 2)} and {(max_col // 2)} < c < {max_col}")

    bot_final_pos = []

    for bot in the_data:
        # calculate the position of the bot after steps
        r = (bot["p"][1] + bot["v"][1] * steps) % max_row
        c = (bot["p"][0] + bot["v"][0] * steps) % max_col
        bot_final_pos.append((r, c))
        if 0 <= r < (max_row // 2) and 0 <= c < (max_col // 2):
            # top-left-quadrant
            quadrants[0] += 1
        elif 0 <= r < (max_row // 2) and (max_col // 2) < c < max_col:
            # top-right-quadrant
            quadrants[1] += 1
        elif (max_row // 2) < r < max_row and (max_col // 2) < c < max_col:
            # bottom-right-quadrant
            quadrants[2] += 1
        elif (max_row // 2) < r < max_row and 0 <= c < (max_col // 2):
            # bottom-left-quadrant
            quadrants[3] += 1
        else:
            print(f"{bot=} is at the floor ({r}, {c})")

    print(f"{quadrants[0]} * {quadrants[1]} * {quadrants[2]} * {quadrants[3]}")
    draw_bot_map(bot_final_pos, max_row, max_col)

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def solve_part2(the_data, steps, max_row, max_col):
    """find shape of christmas tree
     *
    ***

    Args:
        the_data (_type_): _description_
        steps (_type_): _description_
        max_row (_type_): _description_
        max_col (_type_): _description_

    Returns:
        _type_: _description_
    """
    bot_pos = []
    # do a while, until all bots have the starting position (again)
    for step in range(steps):
        bot_pos.clear()
        bots_per_row = [0 for _ in range(max_row)]
        for bot in the_data:
            # calculate the position of the bot after steps
            r = (bot["p"][1] + bot["v"][1] * steps) % max_row
            c = (bot["p"][0] + bot["v"][0] * steps) % max_col
            bots_per_row[r] += 1
            bot_pos.append((r, c))

        print(f"Max bots in a row: {max(bots_per_row)}")

        while 1 in bots_per_row:
            idx = bots_per_row.index(1)
            depth = 1
            expected = 3
            while bots_per_row[idx + depth] == expected:
                depth += 1
                expected += 2
            print(f"Seconds: {step+1}, row: {idx}, depth: {expected}")
            # draw_bot_map(bot_pos, max_row, max_col)
            bots_per_row.remove(1)

    return step


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day14.data")
    # solution1 = solve_part1(the_data, 100, 103, 101)
    solution2 = solve_part2(the_data, 10000000, 103, 101)

    # the_data = get_data("2024/data/day14.test")
    # solution1 = solve_part1(the_data, 100, 7, 11)
    # solution2 = solve_part2(the_data, 100, 7, 11)

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

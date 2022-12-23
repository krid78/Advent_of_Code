#!/usr/bin/env python3
""" Advent of Code 2022/12/23
https://adventofcode.com/2022/day/23
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def get_empty(positions: list) -> int:
    """calculate rect and empty positions"""
    min_x = 1_000_000
    max_x = 0
    min_y = 1_000_000
    max_y = 0
    empty = 0

    for x, y in positions:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    print(f"{(min_x, min_y)}, {(max_x, max_y)}")

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) not in positions:
                empty += 1

    return empty


def get_neighborhood(pos: tuple, positions: list) -> list:
    """check, if any of the eight surrounding fields is occupied
    Return a list of True (free) and False for the 4 directions
    """
    # NW, N, NE, E, SE, S, SW, W
    directions = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
    ]
    # [N, S, W, E]
    status = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    x, y = pos

    for dx, dy in directions:
        if (x + dx, y + dy) in positions:
            if dy == -1:  # N
                status[0] = (0, 0)
            if dy == 1:  # S
                status[1] = (0, 0)
            if dx == -1:  # W
                status[2] = (0, 0)
            if dx == 1:  # E
                status[3] = (0, 0)

    return status


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    # the_data = get_data("data_test2.txt")
    the_data = get_data("data.txt")

    positions = []
    head = 0

    for row, data in enumerate(the_data):
        for col, sym in enumerate(data):
            if sym == "#":
                positions.append((col, row))

    print(get_empty(positions))
    print(positions)

    # progress 10 rounds
    for a_round in range(10):
        new_positions = {}
        # first half
        # all Elves watch their neighbors
        # decide for new postion and claim it
        for x, y in positions:
            new_x, new_y = x, y
            dir_stat = get_neighborhood((x, y), positions)
            if (0, 0) in dir_stat:
                # 0 = N, 1 = S, 2 = W, 3 = E
                for direction in range(head, head + len(dir_stat)):
                    direction %= len(dir_stat)
                    dx, dy = dir_stat[direction]
                    if dx != 0 or dy != 0:
                        new_x = x + dx
                        new_y = y + dy
                        break

            if (new_x, new_y) in new_positions:
                new_positions[(new_x, new_y)].append((x, y))
            else:
                new_positions[(new_x, new_y)] = [(x, y)]

        # second half
        # move the Elves
        # if a position is not overbooked, take it
        # print(new_positions)
        positions.clear()
        for new_pos in new_positions:
            if len(new_positions[new_pos]) > 1:
                positions.extend(new_positions[new_pos])
            else:
                positions.append(new_pos)

        head = (head + 1) % len(dir_stat)
        print(positions)

    solution = get_empty(positions)

    print(f"{solution=}")
    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

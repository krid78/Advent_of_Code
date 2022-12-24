#!/usr/bin/env python3
""" Advent of Code 2022/12/24
https://adventofcode.com/2022/day/24
"""

from collections import deque


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    # the_data = get_data("data_test2.txt")
    the_data = get_data("data.txt")

    b_north = []
    b_south = []
    b_east = []
    b_west = []

    # x, y
    start = (the_data[0].find(".") - 1, -1)
    goal = (the_data[-1].find(".") - 1, len(the_data) - 1)
    width = len(the_data[0]) - 2
    height = len(the_data) - 2

    print(f"From {start} to {goal}")

    # enumerate, offset !
    for row, data in enumerate(the_data[1:-1]):
        for col, blizzard in enumerate(data[1:-1]):
            if blizzard == "^":
                b_north.append((col, row))
            if blizzard == "v":
                b_south.append((col, row))
            if blizzard == ">":
                b_east.append((col, row))
            if blizzard == "<":
                b_west.append((col, row))

    del row
    del col
    del data
    del blizzard

    steps = 0
    solution = -1
    next_nodes = [start]

    while steps < 1_000 and solution <= 0:
        # print("S", end="", flush=True)
        print(f"{steps=}", flush=True)
        nodes = deque(next_nodes)
        next_nodes.clear()

        b_north = [(bx, (by - 1) % height) for bx, by in b_north]
        b_south = [(bx, (by + 1) % height) for bx, by in b_south]
        b_east = [((bx + 1) % width, by) for bx, by in b_east]
        b_west = [((bx - 1) % width, by) for bx, by in b_west]

        next_field = set(b_north + b_south + b_east + b_west)
        # print(f"{steps:=02}, {next_field}")
        #  print(f"{steps:=02}")
        # print(f"{nodes}")

        # https://de.wikibooks.org/wiki/Algorithmensammlung:_Graphentheorie:_Breitensuche
        while len(nodes) > 0:
            # print(".", end="", flush=True)
            node_x, node_y = nodes.popleft()
            # check, if we reached the goal
            if (node_x, node_y) == goal:
                print("found the goal")
                solution = steps
                break
            # find free neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
                next_x, next_y = node_x + dx, node_y + dy
                if (
                    (next_x, next_y) != start
                    and (next_x, next_y) != goal
                    and (next_x < 0 or next_x > width or next_y < 0 or next_y > height)
                ):
                    continue
                if (next_x, next_y) not in next_field:
                    # print(f"candidate: {(next_x, next_y)}")
                    next_nodes.append((next_x, next_y))
                if next_x < 0 or next_x > width or next_y < 0 or next_y > height:
                    print(f"Fatal Error")
            if solution >= 0:
                break

        steps += 1

    print(f"{solution=}")
    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

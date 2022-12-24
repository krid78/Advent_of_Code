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


def draw_field(width, height, blizzards, nodes, start, goal):
    """draw the field"""
    signs = ["^", ">", "v", "<"]
    line = ["#"] * (width + 2)
    if start in nodes:
        line[start[0] + 1] = "E"
    else:
        line[start[0] + 1] = "."
    print("".join(line))
    inner = []

    for y in range(height):
        inner.append(["#"])
        for x in range(width):
            inner[y].append(".")
        inner[y].append("#")

    for idx, b in enumerate(blizzards):
        for x, y in b:
            if inner[y][x + 1] == ".":
                inner[y][x + 1] = signs[idx]
            else:
                inner[y][x + 1] = "*"

    for x, y in nodes:
        if (x, y) == start or (x, y) == goal:
            continue
        if x < 0 or x >= width:
            break
        if y < 0 or y >= height:
            break
        if inner[y][x + 1] == ".":
            inner[y][x + 1] = "E"
        else:
            inner[y][x + 1] = "!"

    for line in inner:
        print("".join(line))

    line = ["#"] * (width + 2)
    if goal in nodes:
        line[goal[0] + 1] = "E"
    else:
        line[goal[0] + 1] = "."
    print("".join(line))


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
    all_start = (the_data[0].find(".") - 1, -1)
    all_goal = (the_data[-1].find(".") - 1, len(the_data) - 2)
    all_time = 0
    width = len(the_data[0]) - 2
    height = len(the_data) - 2

    md = abs(all_goal[0] - all_start[0]) + abs(all_goal[1] - all_start[1])

    print(f"From {all_start} to {all_goal} ({md=})")

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

    next_field = set(b_north + b_south + b_east + b_west)

    del row
    del col
    del data
    del blizzard

    steps = 0
    solution = -1
    start = all_start
    goal = all_goal
    next_nodes = set([start])

    # from start to goal
    while steps < 2000 and solution <= 0:
        # print("S", end="", flush=True)
        nodes = deque(next_nodes)
        next_nodes.clear()

        b_north = [(bx, (by - 1) % height) for bx, by in b_north]
        b_south = [(bx, (by + 1) % height) for bx, by in b_south]
        b_east = [((bx + 1) % width, by) for bx, by in b_east]
        b_west = [((bx - 1) % width, by) for bx, by in b_west]

        next_field = set(b_north + b_south + b_east + b_west)
        # print(f"{steps:=4}, {len(nodes)}, {len(next_field)}", flush=True)

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
                if next_x > width - 1 and next_y > height - 1:
                    pass
                if (
                    (next_x < 0 or next_x >= width or next_y < 0 or next_y >= height)
                    and (next_x, next_y) != start
                    and (next_x, next_y) != goal
                ):
                    continue

                next_nodes.add((next_x, next_y))
            next_nodes = next_nodes - next_field
            if solution >= 0:
                break

        steps += 1

    # store the time
    # steps = solution

    # back to start
    solution = -1
    start = all_goal
    goal = all_start
    next_nodes = set([start])
    while steps < 2000 and solution <= 0:
        # print("S", end="", flush=True)
        nodes = deque(next_nodes)
        next_nodes.clear()

        b_north = [(bx, (by - 1) % height) for bx, by in b_north]
        b_south = [(bx, (by + 1) % height) for bx, by in b_south]
        b_east = [((bx + 1) % width, by) for bx, by in b_east]
        b_west = [((bx - 1) % width, by) for bx, by in b_west]

        next_field = set(b_north + b_south + b_east + b_west)
        # print(f"{steps:=4}, {len(nodes)}, {len(next_field)}", flush=True)

        # https://de.wikibooks.org/wiki/Algorithmensammlung:_Graphentheorie:_Breitensuche
        while len(nodes) > 0:
            # print(".", end="", flush=True)
            node_x, node_y = nodes.popleft()
            # check, if we reached the goal
            if (node_x, node_y) == goal:
                print("found the goal")
                next_nodes.add((next_x, next_y))  # for the drawings
                solution = steps
                break
            # find free neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
                next_x, next_y = node_x + dx, node_y + dy
                if next_x > width - 1 and next_y > height - 1:
                    pass
                if (
                    (next_x < 0 or next_x >= width or next_y < 0 or next_y >= height)
                    and (next_x, next_y) != start
                    and (next_x, next_y) != goal
                ):
                    continue

                next_nodes.add((next_x, next_y))
            next_nodes = next_nodes - next_field
            if solution >= 0:
                break

        steps += 1

    # update time
    # steps = solution

    # back to goal
    solution = -1
    start = all_start
    goal = all_goal
    next_nodes = set([start])
    while steps < 2000 and solution <= 0:
        # print("S", end="", flush=True)
        nodes = deque(next_nodes)
        next_nodes.clear()

        b_north = [(bx, (by - 1) % height) for bx, by in b_north]
        b_south = [(bx, (by + 1) % height) for bx, by in b_south]
        b_east = [((bx + 1) % width, by) for bx, by in b_east]
        b_west = [((bx - 1) % width, by) for bx, by in b_west]

        next_field = set(b_north + b_south + b_east + b_west)
        # print(f"{steps:=4}, {len(nodes)}, {len(next_field)}", flush=True)

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
                if next_x > width - 1 and next_y > height - 1:
                    pass
                if (
                    (next_x < 0 or next_x >= width or next_y < 0 or next_y >= height)
                    and (next_x, next_y) != start
                    and (next_x, next_y) != goal
                ):
                    continue

                next_nodes.add((next_x, next_y))
            next_nodes = next_nodes - next_field
            if solution >= 0:
                break

        steps += 1

    print(f"{solution=}")
    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

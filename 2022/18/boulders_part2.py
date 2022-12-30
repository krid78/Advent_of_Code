#!/usr/bin/env python3
""" Advent of Code 2022/12/18
https://adventofcode.com/2022/day/18
"""

from itertools import combinations
from collections import deque


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [tuple(map(int, row.strip().split(","))) for row in in_file]

    return content


def get_neighbors(point, cmin, cmax):
    neighbors = set()
    for delta in [
        (-1, 0, 0),  # left
        (1, 0, 0),  # right
        (0, -1, 0),  # below
        (0, 1, 0),  # above
        (0, 0, -1),  # in front
        (0, 0, 1),  # behind
    ]:
        a_point = tuple([p + d for p, d in zip(point, delta)])
        if all([d >= cmin and d <= cmax for d in a_point]):
            neighbors.add(a_point)
    return neighbors


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    cubes = set(the_data)

    surface = 0
    # space of the cubes
    cmin = min(min(c) for c in cubes) - 1  # lowest possible coordinate
    cmax = max(max(c) for c in cubes) + 1  # highest possible coordinate
    nodes = deque([(cmin, cmin, cmin)])
    visited = set()
    while nodes:
        node = nodes.pop()
        for neighbor in get_neighbors(node, cmin, cmax):
            if neighbor not in visited:
                if neighbor in cubes:
                    surface += 1
                else:
                    visited.add(neighbor)
                    nodes.append(neighbor)

    return surface


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

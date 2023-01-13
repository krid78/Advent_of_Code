#!/usr/bin/env python3
""" Advent of Code 2022/12/16
https://adventofcode.com/2022/day/16

https://www.geeksforgeeks.org/python-functools-lru_cache/
... reducing the execution time of the function by using memoization technique.
"""

import re
from collections import deque


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def get_valves(data):
    """
    Return a data structure of all valves
    """
    regex = re.compile(
        r"Valve (\w+) has flow rate=(\d+); tunnels* leads* to valves* (.*)"
    )
    valves = {}

    for data in data:
        match = regex.match(data)
        if match:
            valve, flow_rate, connected_valves = match.groups()
        else:
            print("Error parsing")
            continue

        valves[valve] = {
            "fl": int(flow_rate.strip()),
            "conn": connected_valves.split(", "),
        }

    return valves


def nq_sort(status):
    """https://www.youtube.com/watch?v=3-VJC_KRUZ0&t=330s"""
    _, _, r_pressure = status
    return r_pressure


def main():
    """code if module is called directly"""
    the_data = get_data("data_test1.txt")
    # the_data = get_data("data.txt")

    valves = get_valves(the_data)

    minutes = 0

    # current valve, opened valves, time left, pressure released
    next_nodes = [("AA", (), 0)]

    while minutes < 5:
        minutes += 1  # in minute ...
        nodes = deque(sorted(next_nodes, key=nq_sort, reverse=True)[:10000])
        next_nodes.clear()

        while nodes:
            valve, opened, r_pressure = nodes.popleft()

            # pressure in this round
            for o in opened:
                r_pressure += valves[o]["fl"]

            if valve not in opened and valves[valve]["fl"] != 0:
                opened = tuple(opened + (valve,))
                next_nodes.append(
                    (
                        valve,
                        opened,
                        r_pressure,
                    )
                )
            else:
                for subsequent in valves[valve]["conn"]:
                    next_nodes.append(
                        (
                            subsequent,
                            opened,
                            r_pressure,
                        )
                    )

    # store best values
    best = set()
    nodes = deque(sorted(next_nodes, key=nq_sort, reverse=True)[:10000])

    for node in nodes:
        best.add(node[2])

    return max(best)


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

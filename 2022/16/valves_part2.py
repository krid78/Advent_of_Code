#!/usr/bin/env python3
""" Advent of Code 2022/12/16
https://adventofcode.com/2022/day/16

bfs approach

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
    _, _, t_left, r_pressure = status
    return 10 * t_left + 100 * r_pressure


def solve(next_nodes, valves):
    """solve the puzzle"""

    best = set()

    while next_nodes:
        print(f"{len(next_nodes)}")
        nodes = deque(sorted(next_nodes, key=nq_sort, reverse=True)[:50000])
        next_nodes.clear()

        while nodes:
            valve, opened, t_left, r_pressure = nodes.popleft()

            if t_left <= 0:
                best.add(r_pressure)
                continue

            if valve not in opened and valves[valve]["fl"] != 0:
                opened = tuple(opened + (valve,))
                t_left -= 1
                r_pressure += t_left * valves[valve]["fl"]

            for subsequent in valves[valve]["conn"]:
                next_nodes.append(
                    (
                        subsequent,
                        opened,
                        t_left - 1,
                        r_pressure,
                    )
                )

    return opened, best


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    valves = get_valves(the_data)

    # me, opened, t_left, pres
    opened, best = solve([("AA", (), 26, 0)], valves)

    # ele, opened, t_left, pres
    _, best = solve([("AA", (), 26, max(best))], valves)

    return max(best)


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

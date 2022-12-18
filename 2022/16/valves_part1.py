#!/usr/bin/env python3
""" Advent of Code 2022/12/16
https://adventofcode.com/2022/day/16

https://www.geeksforgeeks.org/python-functools-lru_cache/
... reducing the execution time of the function by using memoization technique.
"""

import re
import functools


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


@functools.lru_cache(maxsize=None)
def simulate(valve, time_left, opened):
    """brute force pass all ways"""
    global valves
    cur_flow = 0
    val = 0

    # stop if time's over
    if time_left <= 0:
        return cur_flow

    # open current valve, if closed and has impact
    if valve not in opened:
        if valves[valve]["fl"] != 0:
            time_left -= 1
            val = time_left * valves[valve]["fl"]
            # opened[valve] = val
            opened = tuple(opened + (valve,))

        for subsequent in valves[valve]["conn"]:
            # print(f"{time_left:} from {valve} to {subsequent}")
            cur_flow = max(cur_flow, simulate(subsequent, time_left - 1, opened))
            # print(f"{time_left=}: from {subsequent}: {cur_flow}")

    return val + cur_flow


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    regex = re.compile(
        r"Valve (\w+) has flow rate=(\d+); tunnels* leads* to valves* (.*)"
    )
    global valves
    valves = {}

    for data in the_data:
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

    # for valve in valves:
    #     print(f"{valve}({valves[valve]['fl']}) -> {valves[valve]['conn']}")

    # for valve in valves:
    #     print(f"{valve}, ", end="")
    #     print()

    # for valve in valves:
    #     for next_valve in valves[valve]["conn"]:
    #         print(f"    {valve}[{valve}, {valves[valve]['fl']}] --> {next_valve}")

    # start at AA; have 30 Minutes left
    best = simulate(
        "AA",
        30,
        (),
    )

    return best


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

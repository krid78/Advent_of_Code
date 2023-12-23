#!/usr/bin/env python3
"""Solve Advent of Code 2023/12/06
https://adventofcode.com/2023/day/6
"""

import re

def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content

def calc_wins(rt, rd):
    """Calculate the first win time of a race"""
    for t in range(0, rt):
        # travel distance is (race time - charge time) * speed
        # speed is equal to charge time
        mydist = (rt - t) * t
        if mydist > rd:
            # we will win the race, if mydist is larger than race distance
            # if we found this point, we can calculate the rest easily
            print(f"First win: {mydist=}")
            break
    # we loose race 0, 1, 2, .. t-1 and rt, rt-1, ..., rt-t
    # we loose t*2 races, we will win the rest
    # we need a correction of one (0 .. n is n+1 races)

    return (rt + 1) - (t * 2)

def main():
    """Solve day 06"""
    solution1 = 1
    solution2 = 1

    # the_data = get_data("day06_test1.txt")
    the_data = get_data("day06_data.txt")

    # solve part 1
    # die Funktion ist symetrisch. Es reicht, den ersten "Sieg" zu finden
    # von hinten gesehen ist es dann Länge - 1.Treffer
    rtime = list(map(int, re.findall("\d+", the_data[0])))
    rdist = list(map(int, re.findall("\d+", the_data[1])))
 
    for rt, rd in zip(rtime, rdist):
        wins = calc_wins(rt, rd)

        solution1 *= wins


    # solve part 2
    rt = int("".join([str(x) for x in rtime]))
    rd = int("".join([str(x) for x in rdist]))
    print(f"{rtime=}, {rdist=}")

    solution2 = calc_wins(rt, rd)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1=} | {solution2=}")


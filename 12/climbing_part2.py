#!/usr/bin/env python3
""" Advent of Code 2022/12/12
https://adventofcode.com/2022/day/12


This is a ideal chance to implement a Dijkstra algorithm in python
Unfortunately, creating a tree is a pain
A simple approach seems to iterate over the data and create a map holding the
point and it's neighbors.
{
    (x, y): [(xn, yn), (xn, yn), ...] 
}
With this base, we could implement something like
https://pythonalgos.com/dijkstras-algorithm-in-5-steps-with-python/
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    height_map = []
    steps = []
    start = []

    for heights in the_data:
        height_map.append([ord(c) for c in heights])

    # find all as as start and E as end
    for vert in range(len(height_map)):
        for horz in range(len(height_map[vert])):
            if height_map[vert][horz] == ord("S") or height_map[vert][horz] == ord("a"):
                height_map[vert][horz] = ord("a")
                start.append((vert, horz))
            if height_map[vert][horz] == ord("E"):
                height_map[vert][horz] = ord("z")
                end = (vert, horz)

    candidates = []

    for current in start:
        current = [current]
        step = 0

        for heights in the_data:
            steps.append([-1] * len(heights))

        while step < 1000:
            next = set()
            step += 1
            for vert, horz in current:
                if vert > 0:
                    if height_map[vert - 1][horz] - height_map[vert][horz] <= 1:
                        next.add((vert - 1, horz))
                        if steps[vert - 1][horz] < 0:
                            steps[vert - 1][horz] = step
                        else:
                            steps[vert - 1][horz] = min(step, steps[vert - 1][horz])
                if horz > 0:
                    if height_map[vert][horz - 1] - height_map[vert][horz] <= 1:
                        next.add((vert, horz - 1))
                        if steps[vert][horz - 1] < 0:
                            steps[vert][horz - 1] = step
                        else:
                            steps[vert][horz - 1] = min(step, steps[vert][horz - 1])
                if vert < len(height_map) - 1:
                    if height_map[vert + 1][horz] - height_map[vert][horz] <= 1:
                        next.add((vert + 1, horz))
                        if steps[vert + 1][horz] < 0:
                            steps[vert + 1][horz] = step
                        else:
                            steps[vert + 1][horz] = min(step, steps[vert + 1][horz])
                if horz < len(height_map[0]) - 1:
                    if height_map[vert][horz + 1] - height_map[vert][horz] <= 1:
                        next.add((vert, horz + 1))
                        if steps[vert][horz + 1] < 0:
                            steps[vert][horz + 1] = step
                        else:
                            steps[vert][horz + 1] = min(step, steps[vert][horz + 1])

            if end in next:
                print(f"Hit End after {step} steps")
                candidates.append(step)
                break

            if not next:
                print("No next node, exiting")
                break

            current = list(next)

    candidates.sort()
    print(f"{candidates[0]}")
    return candidates[0]


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

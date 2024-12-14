"""Solve Advent of Code 2015, day 2

https://adventofcode.com/2015/day/2
"""

import time


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    content = []
    with open(filename, "r") as in_file:
        for line in in_file:
            line = line.strip()
            if line:
                l, w, h = map(int, line.split("x"))
                content.append((l, w, h))

    return content


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2015/data/day02.data")
    # the_data = get_data("2015/data/day02.test")

    for l, w, h in the_data:
        s1 = l * w
        s2 = w * h
        s3 = h * l
        solution1 += 2 * (s1 + s2 + s3) + min(s1, s2, s3)
        solution2 += 2 * (l + w + h - max(l, w, h)) + l * w * h

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

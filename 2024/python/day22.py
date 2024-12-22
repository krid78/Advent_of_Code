"""Solve Advent of Code 2024, day 22

https://adventofcode.com/2024/day/22
"""

import time


def get_data(filename: str) -> list[int]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return list(map(int, content))


def next_secret(s: int) -> int:
    # Operation 1: S * 64
    s = ((s << 6) ^ s) & 0xFFFFFF
    # Operation 2: S / 32
    s = ((s >> 5) ^ s) & 0xFFFFFF
    # Operation 3: S * 2048
    s = ((s << 11) ^ s) & 0xFFFFFF
    return s


def solve_intro1(secret: int = 123) -> None:
    """Reproduce the introduction"""
    s0 = secret
    sequence = []

    for _ in range(10):
        s1 = ((s0 * 64) ^ s0) % 16777216
        s2 = ((s1 // 32) ^ s1) % 16777216
        s3 = ((s2 * 2048) ^ s2) % 16777216
        sequence.append(s3)
        s0 = s3

    print(sequence)


def solve_intro2(secret: int = 123) -> None:
    """Reproduce the introduction"""
    s0 = secret
    sequence = []

    for _ in range(10):
        secret = next_secret(secret)
        sequence.append(secret)

    print(sequence)


def solve_part1(the_data: list[int]) -> int:
    """Solve the puzzle.
    s1 = ((s0 * 64) ^ s0) % 16777216
    s2 = ((s1 // 32) ^ s1) % 16777216
    s3 = ((s2 * 2048) ^ s2) % 16777216
    """
    secrets = []

    for s0 in the_data:
        for _ in range(2000):
            s0 = next_secret(s0)
        secrets.append(s0)

    return sum(secrets)


def solve_part2(the_data: list[int]) -> int:
    """Solve the puzzle."""
    solution = 0

    return solution


if __name__ == "__main__":

    time_start = time.perf_counter()
    solve_intro1(123)
    print(f"Intro solved in {time.perf_counter()-time_start:.5f} Sec.")

    time_start = time.perf_counter()
    solve_intro2(123)
    print(f"Intro solved in {time.perf_counter()-time_start:.5f} Sec.")

    the_data = get_data("2024/data/day22.data")
    # the_data = get_data("2024/data/day22.test")

    # solve part 1
    time_start = time.perf_counter()
    solution1 = solve_part1(the_data)
    print(f"Part 1 ({solution1}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # solve part 2
    time_start = time.perf_counter()
    solution2 = solve_part2(the_data)
    print(f"Part 2 ({solution2}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # finally
    print(f"{solution1=} | {solution2=}")

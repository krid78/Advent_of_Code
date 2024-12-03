"""Solve Advent of Code 2024, day 3

https://adventofcode.com/2024/day/3
"""

import re


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def solve1(the_data):
    """Solve part 1"""
    pattern1 = r"mul\(\d{1,3},\d{1,3}\)"
    pattern2 = r"\d{1,3}"

    matches = re.findall(pattern1, "".join(the_data))
    # print(matches)

    solution = 0
    for mul in matches:
        numbers = re.findall(pattern2, mul)
        # print(numbers)
        solution += int(numbers[0]) * int(numbers[1])

    return solution


def solve2(the_data):
    """Solve part 2"""
    pattern1 = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    pattern2 = r"\d{1,3}"

    matches = re.findall(pattern1, "".join(the_data))
    # print(matches)

    solution = 0
    mode = "do()"
    for tok in matches:
        if tok in ["do()", "don't()"]:
            mode = tok
        elif mode == "do()":
            numbers = re.findall(pattern2, tok)
            # print(numbers)
            solution += int(numbers[0]) * int(numbers[1])
        else:
            pass

    return solution


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day03.data")
    # the_data = get_data("2024/data/day03_01.test")
    # the_data = get_data("2024/data/day03_02.test")

    solution1 = solve1(the_data)
    solution2 = solve2(the_data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
    print(f"{solution1=} | {solution2=}")

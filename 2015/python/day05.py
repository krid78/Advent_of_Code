"""Solve Advent of Code 2015, day 5

https://adventofcode.com/2015/day/5
"""

import time


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def solve_part1(the_data: list[str]) -> int:
    """Solve the puzzle."""
    solution = 0

    for nice_string in the_data:
        twice = False
        vowels = [x for x in nice_string if x in "aeiou"]
        if len(vowels) < 3:
            continue
        for idx in range(0, len(nice_string) - 1):
            if nice_string[idx] == nice_string[idx + 1]:
                twice = True
                break
        if not twice:
            continue
        if (
            nice_string.find("ab") > 0
            or nice_string.find("cd") > 0
            or nice_string.find("pq") > 0
            or nice_string.find("xy") > 0
        ):
            continue
        solution += 1

    return solution


def solve_part2(the_data: list[str]) -> int:
    """Solve the puzzle."""
    solution = 0

    for nice_string in the_data:
        nsl = len(nice_string)
        twice = False
        repeated = False
        for idx in range(nsl - 1):
            pattern = nice_string[idx : idx + 2]
            pcount = nice_string.count(pattern)
            if pcount > 1:
                repeated = True
                break
        for idx in range(nsl - 2):
            if nice_string[idx] == nice_string[idx + 2]:
                twice = True
                break
        if not twice or not repeated:
            continue
        print(f"{nice_string} is nice for part 2")
        solution += 1
    return solution


def main(test=False):
    """Use main function to avoid global variables"""
    if test:
        # the_data = get_data("2015/data/day05.test")
        # the_data = ["xyxy", "aabcdefgaa", "aaa", "xyx", "abcdefeghi"]
        the_data = [
            "aaa",
            "ieodomkazucvgmuy",
            "qjhvhtzxzqqjkmpb",
            "uurcxstgmygtbstg",
            "xxyxx",
        ]
    else:
        the_data = get_data("2015/data/day05.data")

    # Solve part 1
    time_start = time.perf_counter()
    solution1 = solve_part1(the_data)
    print(f"Part 1 ({solution1}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # solve part 1
    time_start = time.perf_counter()
    solution2 = solve_part2(the_data)
    print(f"Part 2 ({solution2}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # Finally
    print(f"{solution1=} | {solution2=}")


if __name__ == "__main__":
    main(test=False)

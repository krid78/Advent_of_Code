"""Solve Advent of Code 2024, day 2

https://adventofcode.com/2024/day/2
"""


def get_data(filename: str) -> list[str]:
    """Return file contents as a list of strings."""
    with open(filename, "r") as in_file:
        return [row.rstrip() for row in in_file]


def check_report(report: list[str]) -> tuple[bool, int]:
    """
    Check the given report for the specified conditions.

    Args:
        report: List of stringified integers in the report.

    Returns:
        A tuple containing:
        - A boolean indicating if the report is valid.
        - The index where the first failure occurs (or the last checked index if valid).
    """
    res = False
    diff = int(report[0]) - int(report[1])

    if 0 < diff < 4:
        safe = {1, 2, 3}
    elif -4 < diff < 0:
        safe = {-1, -2, -3}
    else:
        return res, 0

    for idx in range(1, len(report) - 1):
        check = int(report[idx]) - int(report[idx + 1])
        if check not in safe:
            return res, idx

    return True, len(report) - 2


def try_fix_report(report: list[str], idx: int) -> bool:
    """
    Try fixing the report by removing problematic entries.

    Args:
        report: List of stringified integers in the report.
        idx: Index of the first problematic entry.

    Returns:
        A boolean indicating if the report is valid after fixing.
    """
    # Try dropping the current element
    res, _ = check_report(report[:idx] + report[idx + 1 :])
    if res:
        return True

    # Try dropping the next element
    res, _ = check_report(report[: idx + 1] + report[idx + 2 :])
    if res:
        return True

    # Try dropping the first element if idx is within the first 2 elements
    if idx < 2:
        res, _ = check_report(report[1:])
        return res

    return False


def solve1(the_data: list[str]) -> int:
    """
    Solve part 1 of the puzzle.

    Args:
        the_data: List of input lines from the puzzle file.

    Returns:
        The solution for part 1.
    """
    solution = 0
    for line in the_data:
        report = line.split()
        res, _ = check_report(report)
        if res:
            solution += 1
    return solution


def solve2(the_data: list[str]) -> int:
    """
    Solve part 2 of the puzzle.

    Args:
        the_data: List of input lines from the puzzle file.

    Returns:
        The solution for part 2.
    """
    solution = 0
    for line in the_data:
        report = line.split()
        res, idx = check_report(report)
        if not res:
            res = try_fix_report(report, idx)
        if res:
            solution += 1
    return solution


def solve() -> tuple[int, int]:
    """
    Solve the puzzle for both parts.

    Returns:
        A tuple containing solutions for part 1 and part 2.
    """
    # Load data
    the_data = get_data(
        "/home/dkrieste/Dokumente/Develop/advent-of-code/2024/data/day02.data"
    )
    # the_data = get_data(
    #     "/home/dkrieste/Dokumente/Develop/advent-of-code/2024/data/day02.test"
    # )

    solution1 = solve1(the_data)
    solution2 = solve2(the_data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
    print(f"{solution1=} | {solution2=}")

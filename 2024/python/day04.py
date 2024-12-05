"""Solve Advent of Code 2024, day 4

https://adventofcode.com/2024/day/4
"""


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def find_xmas(data: list[str], row: int, col: int, direction: tuple[int, int]) -> int:
    """
    Find the term 'XMAS' in the given direction starting at (row, col).

    Args:
        data: List of strings representing the grid.
        row: Starting row index.
        col: Starting column index.
        direction: Tuple (dr, dc) representing the direction to search.

    Returns:
        1 if 'XMAS' is found, 0 otherwise.
    """
    dr, dc = direction

    # Check bounds for the 4-character substring
    if not (0 <= row + 3 * dr < len(data) and 0 <= col + 3 * dc < len(data[0])):
        return 0

    # Check if the characters form 'XMAS'
    return all(data[row + i * dr][col + i * dc] == "XMAS"[i] for i in range(4))


def find_mas(data: list[str], row: int, col: int):
    """Find 2 times MAS in the shape of an X
    M.M | M.S | S.M | S.S
    .A. | .A. | .A. | .A.
    S.S | M.S | S.M | M.M
    """
    # Check bounds for the 4-character substring
    if not (0 < row < len(data) - 1 and 0 < col < len(data[0]) - 1):
        return 0

    foo = ""
    for dr, dc in [(-1, -1), (0, 0), (1, 1)]:
        foo += data[row + dr][col + dc]

    bar = ""
    for dr, dc in [(-1, 1), (0, 0), (1, -1)]:
        bar += data[row + dr][col + dc]

    if (foo == "MAS" or foo[::-1] == "MAS") and (bar == "MAS" or bar[::-1] == "MAS"):
        return 1

    return 0


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day04.data")
    # the_data = get_data("2024/data/day04.test")
    # Define all directions (row, col) deltas
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (0, -1),  # left
        (-1, 0),  # up
        (1, 1),  # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
        (-1, -1),  # diagonal up-left
    ]

    for row in range(len(the_data)):
        for col in range(len(the_data[0])):
            if the_data[row][col] == "X":
                for direction in directions:
                    solution1 += find_xmas(the_data, row, col, direction)

    for row in range(len(the_data)):
        for col in range(len(the_data[0])):
            if the_data[row][col] == "A":
                solution2 += find_mas(the_data, row, col)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
    print(f"{solution1=} | {solution2=}")

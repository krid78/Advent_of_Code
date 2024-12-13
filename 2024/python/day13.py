"""Solve Advent of Code 2024, day 13

https://adventofcode.com/2024/day/13
"""

import time


def get_data(filename: str) -> list[dict[str, tuple[int, int]]]:
    """
    Return file contents as a structured list of dictionaries.

    Args:
        filename (str): Path to the input file.

    Returns:
        list[dict[str, tuple[int, int]]]: A list of dictionaries, where each dictionary
        contains the coordinates for Button A, Button B, and the Prize.
    """
    data = []
    with open(filename, "r") as in_file:
        lines = [line.strip() for line in in_file if line.strip()]

    for i in range(0, len(lines), 3):  # Process blocks of 3 lines
        button_a = parse_coordinates(lines[i])
        button_b = parse_coordinates(lines[i + 1])
        prize = parse_coordinates(lines[i + 2], fixed=True)
        data.append({"ButtonA": button_a, "ButtonB": button_b, "Prize": prize})

    return data


def parse_coordinates(line: str, fixed: bool = False) -> tuple[int, int]:
    """
    Parse a line containing coordinates into a tuple of integers.

    Args:
        line (str): The line containing coordinate information.
        fixed (bool): If True, parses 'X=...' and 'Y=...'. Otherwise, parses 'X+...' and 'Y+...'.

    Returns:
        tuple[int, int]: A tuple (X, Y) representing the coordinates.
    """
    if fixed:
        x = int(line.split("X=")[1].split(",")[0])
        y = int(line.split("Y=")[1])
    else:
        x = int(line.split("X+")[1].split(",")[0])
        y = int(line.split("Y+")[1])
    return x, y


def solve_linear_system_all_solutions(x_a, x_b, p_x, y_a, y_b, p_y):
    """
    Solve the linear system of equations and find all valid solutions.

    Args:
        x_a, x_b, p_x: Coefficients and target for the first equation.
        y_a, y_b, p_y: Coefficients and target for the second equation.

    Returns:
        list[tuple[int, int]]: All valid solutions (a, b).
    """
    solutions = []

    for a in range(101):
        # Compute b for the first equation
        numerator = p_x - a * x_a
        if numerator % x_b != 0:  # b must be an integer
            continue

        b = numerator // x_b

        # Check constraints on b
        if 0 <= b <= 100:
            # Verify the second equation
            if a * y_a + b * y_b == p_y:
                solutions.append((a, b))

    return solutions


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day13.data")
    # the_data = get_data("2024/data/day13.test")

    for claw_machine in the_data:

        solutions = solve_linear_system_all_solutions(
            x_a=claw_machine["ButtonA"][0],
            x_b=claw_machine["ButtonB"][0],
            p_x=claw_machine["Prize"][0],
            y_a=claw_machine["ButtonA"][1],
            y_b=claw_machine["ButtonB"][1],
            p_y=claw_machine["Prize"][1],
        )

        if len(solutions) == 1:
            # print(f"Eindeutige Lösung: {solutions[0]}")
            solution1 += solutions[0][0] * 3 + solutions[0][1]
        elif len(solutions) > 1:
            print(f"Mehrere Lösungen: {solutions}")
        else:
            # print("Keine Lösung gefunden.")
            pass

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

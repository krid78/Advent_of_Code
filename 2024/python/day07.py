"""Solve Advent of Code 2024, day 7

https://adventofcode.com/2024/day/7
"""

import time
from itertools import product


def get_data(filename: str) -> list:
    """Return file contents as list"""
    data = []
    with open(filename, "r") as in_file:
        for line in in_file:
            left, right = line.split(":")
            result = int(left.strip())
            numbers = list(map(int, right.strip().split()))
            data.append((result, numbers))

    return data


def solve_equation(target: int, numbers: list[int], operators: list[str]) -> int:
    """
    Check if the target can be computed using the numbers with addition and multiplication.
    """
    # Generate all possible operator combinations (+ or *) for the numbers
    operators = list(product(operators, repeat=len(numbers) - 1))

    # Test each operator combination
    for ops in operators:
        # Compute the result from left to right
        result = numbers[0]
        for num, op in zip(numbers[1:], ops):
            if op == "+":
                result += num
            elif op == "*":
                result *= num
            elif op == "|":
                result = int(str(result) + str(num))

        # Check if the result matches the target
        if result == target:
            return result

    return 0


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day07.data")
    # the_data = get_data("2024/data/day07.test")

    """ only * and + available
    always left to right"""
    for result, operands in the_data:
        solution1 += solve_equation(result, operands, ["+", "*"])
        solution2 += solve_equation(result, operands, ["+", "*", "|"])

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

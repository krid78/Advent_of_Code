"""Prepare an AoC-day

Create a python template with a correct header
and some boilerplate code

python prepare_day.py --year 2021 --day 22

Prepare for current year and current day, if no year or day are given
"""

import os
import argparse
from datetime import datetime

__TEMPLATE__ = '''"""Solve Advent of Code {year}, day {day}

https://adventofcode.com/{year}/day/{day}
"""


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    # the_data = get_data("day{day:02}.data")
    the_data = get_data("day{day:02}.test")

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
'''

def prepare_day(year, day):
    # Create directory if it doesn't exist
    directory_name = str(year)
    os.makedirs(directory_name, exist_ok=True)
    print(f"Directory '{directory_name}' and files", end="")

    # Create file with the specified day number
    file_name = f"day{day:02}.py"
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as file:
        file.write(__TEMPLATE__.format(**{"year":year, "day":day}))
        file.write('    print(f"{solution1=} | {solution2=}"\n')

    print(f" '{file_name}'", end="")

    file_name = f"day{day:02}.data"
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as file:
        pass  # Empty file

    print(f", '{file_name}'", end="")

    file_name = f"day{day:02}.test"
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as file:
        pass  # Empty file

    print(f" and '{file_name}'", end="")

    print(f" created successfully.")

def main():
    parser = argparse.ArgumentParser(description='Prepare day directory and file.')
    parser.add_argument('-y', '--year', type=int, help='Four-digit year (default: current year)')
    parser.add_argument('-d', '--day', type=int, help='Day number (default: current day)')
    args = parser.parse_args()

    args = parser.parse_args()

    # Use current year if not provided
    year = args.year or datetime.now().year

    # Use current day if not provided
    day = args.day or datetime.now().day

    prepare_day(year, day)

if __name__ == "__main__":
    main()


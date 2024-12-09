"""Prepare an Advent of Code day.

Creates a Python template with a correct header and boilerplate code.

Usage:
    python prepare_day.py --year 2021 --day 22

If no year or day are provided, defaults to the current year and day.
"""

import os
import argparse
from datetime import datetime
import logging

__TEMPLATE__ = '''"""Solve Advent of Code {year}, day {day}

https://adventofcode.com/{year}/day/{day}
"""

import time

def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    # the_data = get_data("{data_dir}day{day:02}.data")
    the_data = get_data("{data_dir}day{day:02}.test")

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {{time.perf_counter()-time_start:.5f}} Sec.")
    print(f"{{solution1=}} | {{solution2=}}")
'''


def create_directory(directory: str) -> None:
    """Create a directory if it doesn't already exist."""
    os.makedirs(directory, exist_ok=True)
    logging.info(f"Directory '{directory}' ensured.")


def write_file(filepath: str, content: str = "") -> None:
    """Write content to a file, or create an empty file if no content is provided."""
    with open(filepath, "w") as file:
        file.write(content)
    logging.info(f"File '{filepath}' created.")


def prepare_day(year: int, day: int) -> None:
    """
    Prepare files and directories for a given Advent of Code day.

    Args:
        year (int): The year of the Advent of Code.
        day (int): The day number.
    """
    # Validate inputs
    if not (1 <= day <= 25):
        raise ValueError("Day must be between 1 and 25.")

    code_dir = os.path.join(str(year), "python")
    data_dir = os.path.join(str(year), "data")
    create_directory(code_dir)
    create_directory(data_dir)

    # Create Python script
    script_path = os.path.join(code_dir, f"day{day:02}.py")
    script_content = __TEMPLATE__.format(year=year, day=day, data_dir=data_dir + os.sep)
    write_file(script_path, script_content)

    # Create data files
    data_path = os.path.join(data_dir, f"day{day:02}.data")
    test_path = os.path.join(data_dir, f"day{day:02}.test")
    write_file(data_path)
    write_file(test_path)

    logging.info(f"Preparation complete for year {year}, day {day}.")


def main():
    parser = argparse.ArgumentParser(
        description="Prepare files for an Advent of Code day."
    )
    parser.add_argument("-y", "--year", type=int, help="Year (default: current year).")
    parser.add_argument(
        "-d", "--day", type=int, help="Day number (default: current day)."
    )
    args = parser.parse_args()

    # Default to current year and day if not provided
    year = args.year or datetime.now().year
    day = args.day or datetime.now().day

    # Prepare files and directories
    try:
        prepare_day(year, day)
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()

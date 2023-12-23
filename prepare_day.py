"""Prepare an AoC-day

Create a python template with a correct header
and some boilerplate code

python prepare_day.py --year 2021 --day 22

Prepare for current year and current day, if no year or day are given
"""

import os
import argparse
from datetime import datetime


def prepare_day(year, day):
    # Create directory if it doesn't exist
    directory_name = str(year)
    os.makedirs(directory_name, exist_ok=True)

    # Create file with the specified day number
    file_name = f"day{day}.py"
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as file:
        pass  # Empty file

    file_name = f"day{day}.data"
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as file:
        pass  # Empty file

    file_name = f"day{day}.test"
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as file:
        pass  # Empty file

    print(f"Directory '{directory_name}' and file '{file_name}' created successfully.")

def main():
    parser = argparse.ArgumentParser(description='Prepare day directory and file.')
    parser.add_argument('--year', type=int, help='Four-digit year (default: current year)')
    parser.add_argument('--day', type=int, help='Day number (default: current day)')
    args = parser.parse_args()

    # Use current year if not provided
    year = args.year or datetime.now().year

    # Use current day if not provided
    day = args.day or datetime.now().day

    prepare_day(year, day)

if __name__ == "__main__":
    main()


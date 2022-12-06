#!/usr/bin/env python3
""" Advent of Code 2022/12/05
https://adventofcode.com/2022/day/5
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open("data.txt", "r") as in_file:
        content = [line.strip() for line in in_file]

    return content


def main():
    the_data = get_data("data_test.txt")

    for line in the_data:
        print(line)
        for idx in range(len(line) - 3):
            print(f"Trying: line[idx:idx+4]")
            if len(set(line[idx : idx + 4])) == 4:
                print(f"Found marker from {idx=} to {(idx + 4)=}")
                break


if __name__ == "__main__":
    main()

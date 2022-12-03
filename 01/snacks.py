#! /usr/bin/env python3
""" Advent of Code 2022/12/01
https://adventofcode.com/2022/day/1
"""


def main():
    """
    the main function of the module
    """
    with open("data.txt", "r") as in_file:
        inventory = [line.strip() for line in in_file]

    cal = [0]

    for item in inventory:
        if item == "":
            cal.append(0)
        else:
            cal[-1] += int(item)

    print(f"Max calories is {max(cal)}")


if __name__ == "__main__":
    main()

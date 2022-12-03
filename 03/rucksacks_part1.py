#!/usr/bin/env python3
""" Advent of Code 2022/12/03
https://adventofcode.com/2022/day/3
"""
import string


def main():
    """
    the main function of the module
    """
    with open("data.txt", "r") as in_file:
        rucksacks = [line.strip() for line in in_file]
    total = 0
    for rucksack in rucksacks:
        size = len(rucksack)
        print(f"{size=}")
        items_c1 = list(rucksack[: size // 2])
        items_c2 = list(rucksack[size // 2 :])
        print(f"{items_c1}")
        print(f"{items_c2}")
        equal = list(set(items_c1) & set(items_c2))
        equal_val = ord(equal[0])
        print(f"{equal=}/{equal_val}")
        total += list(string.ascii_letters).index(equal[0]) + 1

    print(f"Total: {total}")


if __name__ == "__main__":
    main()

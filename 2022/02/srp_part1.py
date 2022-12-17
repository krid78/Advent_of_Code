#!/usr/bin/env python3
""" Advent of Code 2022/12/02
https://adventofcode.com/2022/day/2
"""


def main():
    """
    the main function of the module
    """

    p1_base = ["A", "B", "C"]
    p2_base = ["X", "Y", "Z"]
    score = {
        -2: 0,
        -1: 6,
        0: 3,
        1: 0,
        2: 6,
    }
    total = 0

    with open("data.txt", "r") as in_file:
        rounds = [line.strip() for line in in_file]

    for choices in rounds:
        choice_p1 = p1_base.index(choices.split()[0])
        choice_p2 = p2_base.index(choices.split()[1])
        result = choice_p1 - choice_p2
        total += choice_p2 + 1 + score[result]
        print(f"P1: {p1_base[choice_p1]}; P2: {p2_base[choice_p2]}: {result}")

    print(f"Total: {total}")


if __name__ == "__main__":
    main()

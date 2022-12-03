#!/usr/bin/env python3
""" Advent of Code 2022/12/02
https://adventofcode.com/2022/day/2
"""


def main():
    """
    the main function of the module
    """
    p_base = ["A", "B", "C"]  # Rock, Paper, Scissor

    t_base = {
        "X": (-1, 0),  # P2 loose
        "Y": (0, 3),  # draw
        "Z": (-2, 6),  # P2 win
    }
    total = 0

    with open("data.txt", "r") as in_file:
        rounds = [line.strip() for line in in_file]

    for choices in rounds:
        choice_p1 = p_base.index(choices.split()[0])
        target = t_base[choices.split()[1]][0]
        choice_p2 = p_base[choice_p1 + target]
        print(
            f"Strategy {choices.split()[1]}, P1 chooses {choices.split()[0]}, "
            "we choose {choice_p2}"
        )
        total += t_base[choices.split()[1]][1] + p_base.index(choice_p2) + 1

    print(f"Total: {total}")


if __name__ == "__main__":
    main()

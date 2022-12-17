"""Advent of Code 2021
https://adventofcode.com/2021/day/1
"""


def main():
    """
    main function of this module
    """

    with open("day1_data.txt", "r") as in_file:
        measures = [int(line.strip()) for line in in_file.readlines()]

    count = 0

    for idx in range(len(measures)-3):
        win_a = sum(measures[idx:idx+3])
        win_b = sum(measures[idx+1:idx+4])
        if (win_b > win_a):
            count += 1

    print(f"Increases: {count}")


if __name__ == "__main__":
    main()

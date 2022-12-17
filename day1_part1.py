"""Advent of Code 2021
https://adventofcode.com/2021/day/1
"""


def main():
    """
    main function of this module
    """

    with open("day1_data.txt", "r") as in_file:
        measures = [int(line.strip()) for line in in_file.readlines()]

    analyses = [
        0,
    ]
    count = 0

    for idx, depth in enumerate(measures[1:]):
        if depth > measures[idx]:
            analyses.append(1)
            count += 1
        else:
            analyses.append(0)

    for idx in range(len(measures)):
        if analyses[idx] == 1:
            print(f"{measures[idx]}: increase")
        else:
            print(f"{measures[idx]}: decrease")

    print(f"Increases: {analyses.count(1)}/{count}")


if __name__ == "__main__":
    main()

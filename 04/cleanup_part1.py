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
        assignment_list = [line.strip() for line in in_file]

    total = 0
    for assignments in assignment_list:
        assignment_e1 = assignments.split(",")[0].split("-")
        assignment_e2 = assignments.split(",")[1].split("-")
        print(f"{assignment_e1=}, {assignment_e2=}")
        if int(assignment_e1[0]) >= int(assignment_e2[0]) and int(
            assignment_e1[1]
        ) <= int(assignment_e2[1]):
            total += 1
        elif int(assignment_e2[0]) >= int(assignment_e1[0]) and int(
            assignment_e2[1]
        ) <= int(assignment_e1[1]):
            total += 1
        else:
            pass

    print(f"Total: {total}")


if __name__ == "__main__":
    main()

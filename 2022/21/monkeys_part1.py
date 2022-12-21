#!/usr/bin/env python3
""" Advent of Code 2022/12/21
https://adventofcode.com/2022/day/21
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def solve(_monkeys: dict, name: str):
    """rekursive solve puzzle"""

    if type(_monkeys[name]) == int:
        return _monkeys[name]

    operand1 = solve(_monkeys, _monkeys[name][0])
    operand2 = solve(_monkeys, _monkeys[name][2])
    res = eval(f"{operand1} {_monkeys[name][1]} {operand2}")
    return res


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    monkeys = {}

    for data in the_data:
        monkey, knowledge = tuple(data.split(":"))
        knowledge = knowledge.strip().split()

        if len(knowledge) > 1:
            monkeys[monkey.strip()] = knowledge
        else:
            monkeys[monkey.strip()] = int(knowledge[0])

    solution = solve(monkeys, "root")

    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

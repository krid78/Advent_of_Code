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


def monkey_solve(_monkeys: dict, name: str):
    """rekursive solve puzzle"""

    if type(_monkeys[name]) == int or name == "humn":
        return _monkeys[name]

    operand1 = monkey_solve(_monkeys, _monkeys[name][0])
    operand2 = monkey_solve(_monkeys, _monkeys[name][2])

    res = f"{operand1} {_monkeys[name][1]} {operand2}"
    if name == "root":
        pass
    elif res.find("humn") < 0:
        res = eval(res)
    else:
        res = f"( {res} )"
    return res


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    monkeys = {}

    for data in the_data:
        monkey, knowledge = tuple(data.split(":"))
        knowledge = knowledge.strip().split()
        if monkey.strip() == "humn":
            monkeys[monkey.strip()] = "humn"
        elif monkey.strip() == "root":
            monkeys[monkey.strip()] = [knowledge[0], "==", knowledge[2]]
        elif len(knowledge) > 1:
            monkeys[monkey.strip()] = knowledge
        else:
            monkeys[monkey.strip()] = int(knowledge[0])

    solution = monkey_solve(monkeys, "root")
    solution_left, solution_right = tuple(solution.split("=="))

    # a little bit of cheating
    from sympy.solvers import solve
    from sympy import Symbol

    humn = Symbol("humn")
    solution = eval(f"solve({solution_left} - {solution_right}, humn)")

    return int(solution[0])


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

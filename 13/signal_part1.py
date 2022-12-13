#!/usr/bin/env python3
""" Advent of Code 2022/12/12
https://adventofcode.com/2022/day/12
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def compare_int(left, right):
    """compare int items"""
    return left - right


def compare_lists(left, right):
    """compare items of a list"""
    print(f"comparing {left} to {right}")

    while len(left) > 0 and len(right) > 0:
        lft = left.pop(0)
        rgt = right.pop(0)
        if type(lft) == type(rgt) == int:
            cmp = compare_int(lft, rgt)
        else:  # lists or mixed, compare as lists
            cmp = compare_lists(to_list(lft), to_list(rgt))

        if cmp != 0:
            return cmp
    else:
        return len(left) - len(right)

    print("!! No result !!")
    return 1


def to_list(x):
    """convert x to list"""
    if type(x) == list:
        return x
    elif type(x) == int:
        return [x]
    else:
        return []


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    msg = 0
    candidates = []
    while msg < len(the_data):
        left = eval(the_data[msg])
        right = eval(the_data[msg + 1])
        msg += 3

        if compare_lists(left, right) < 0:
            candidates.append(msg // 3)

    print(candidates)
    return sum(candidates)


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

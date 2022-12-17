#!/usr/bin/env python3
""" Advent of Code 2022/12/13
https://adventofcode.com/2022/day/13

Bubble sort is really slow, could have used quicksort or something else

Hint: 
import functools
the_data.sort(key=functools.cmp_to_key(compare_lists))
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
    the_data.append("[[2]]")
    the_data.append("[[6]]")

    for msg in the_data:
        if msg == "":
            the_data.remove(msg)

    for end in range(len(the_data), 1, -1):
        for item in range(0, end - 1):
            left = eval(the_data[item])
            right = eval(the_data[item + 1])

            if compare_lists(left, right) >= 0:
                tmp = the_data[item]
                the_data[item] = the_data[item + 1]
                the_data[item + 1] = tmp

    return (the_data.index("[[2]]") + 1) * (the_data.index("[[6]]") + 1)


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

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


# def main():
"""code if module is called directly"""
# the_data = get_data("data_test1.txt")
the_data = get_data("data.txt")

monkeys = {}

for data in the_data:
    try:
        monkey, knowledge = tuple(data.split(":"))
        monkeys[monkey.strip()] = knowledge.strip()
    except ValueError:
        print(f"ValueError\n  {data=}")
        knowledge = None

    if type(knowledge) == str and len(knowledge.strip().split()) > 3:
        print(f"{knowledge.split()}")
        break

print(f"root: {monkeys['root']}")

    

    # return best


# if __name__ == "__main__":
#     solution = main()
#     print(f"{solution=}")

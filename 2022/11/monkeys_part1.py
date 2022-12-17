#!/usr/bin/env python3
""" Advent of Code 2022/12/11
https://adventofcode.com/2022/day/11
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


class Monkey(object):
    """this is a Monkey"""

    def __init__(self) -> None:
        self.items = []
        self.equation = ""
        self.test = 1
        self.pass_true = 0
        self.pass_false = 0
        self.inspected = 0

    def calc_worry(self, old):
        """calculate the worry - q&d solution!"""
        return eval(self.equation)

    def get_pass(self, dut):
        """see who gets the item"""
        ret_val = self.pass_false
        if dut % self.test == 0:
            ret_val = self.pass_true

        return ret_val

    def num_items(self):
        """return current number of items"""
        return len(self.items)

    def process_item(self):
        """process an item, return item and target-monkey"""
        w_new, pass_to = None, None
        if self.items:
            w_new = self.calc_worry(self.items.pop(0)) // 3
            pass_to = self.get_pass(w_new)
            self.inspected += 1

        return w_new, pass_to

    def __str__(self):
        return f"""This monkey
\tholds {self.items},
\thas {self.inspected} items inspected,
\tcalculates using: {self.equation} and
\tTest with {self.test}
\tto give its items to {self.pass_true} or {self.pass_false}"""


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test.txt")
    the_data = get_data("data.txt")

    """a monkey as map
    monkey = {
        "items": [],
        "equation": "",
        "if_true": 0,
        "if_false": 0,
        "processed": 0,
    }
    """

    monkeys = []

    for line in the_data:
        if line.startswith("Monkey"):
            monkeys.append(Monkey())
        elif line.startswith("Starting"):
            items = line.split(":")[1].strip()
            monkeys[-1].items.extend(list(eval(f"{items},")))
        elif line.startswith("Operation"):
            monkeys[-1].equation = line.split("=")[1].strip()
        elif line.startswith("Test"):
            monkeys[-1].test = int(line.split(" ")[3].strip())
        elif line.startswith("If true"):
            monkeys[-1].pass_true = int(line.split(" ")[5].strip())
        elif line.startswith("If false"):
            monkeys[-1].pass_false = int(line.split(" ")[5].strip())

    activity = []
    for _ in range(20):
        for monkey in monkeys:
            for _ in range(monkey.num_items()):
                item, pass_to = monkey.process_item()
                if item is not None:
                    monkeys[pass_to].items.append(item)

    for monkey in monkeys:
        activity.append(monkey.inspected)

    activity.sort(reverse=True)
    print(f"monkey business: {activity[0]*activity[1]}")

    return monkeys, activity


if __name__ == "__main__":
    monkeys, activity = main()

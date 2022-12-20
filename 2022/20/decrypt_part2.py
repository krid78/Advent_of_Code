#!/usr/bin/env python3
""" Advent of Code 2022/12/20
https://adventofcode.com/2022/day/20

To mix the file, move each number forward or backward in the file a number of
positions equal to the value of the number being moved. The list is circular,
so moving a number off one end of the list wraps back around to the other end
as if the ends were connected.
"""


class Node(object):
    decryption_key = 811589153

    def __init__(self, idx: int, data: str):
        self.c_idx = idx
        self.value = int(data) * self.decryption_key

    def __str__(self):
        # return f"""{self.value=}, {self.c_idx=}"""
        return f"""{self.value}"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    encrypted = []
    the_data_len = len(the_data) - 1

    # cycle through the input value by value
    for idx, str_shift in enumerate(the_data):
        encrypted.append(Node(idx, str_shift))
        if str_shift == "0":
            null = encrypted[-1]

    decrypted = encrypted.copy()
    for _ in range(10):
        for idx, node in enumerate(encrypted):
            # find the current position of value in target list
            d_idx = decrypted.index(node)

            shift = (d_idx + node.value) % the_data_len

            tmp = decrypted.pop(d_idx)
            decrypted.insert(shift, tmp)

        # print(f"{[str(d.value) for d in decrypted]}")

    c0_idx = decrypted.index(null)
    print(decrypted[c0_idx])
    the_data_len += 1
    c1_idx = (c0_idx + 1000) % the_data_len
    c2_idx = (c0_idx + 2000) % the_data_len
    c3_idx = (c0_idx + 3000) % the_data_len

    print(f"{c0_idx:3}, {c1_idx:3}, {c2_idx:3}, {c3_idx:3}")
    print(
        f"{decrypted[c0_idx].value:3}, "
        f"{decrypted[c1_idx].value:3}, "
        f"{decrypted[c2_idx].value:3}, "
        f"{decrypted[c3_idx].value:3}"
    )
    solution = (
        int(decrypted[c1_idx].value)
        + int(decrypted[c2_idx].value)
        + int(decrypted[c3_idx].value)
    )
    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

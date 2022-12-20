#!/usr/bin/env python3
""" Advent of Code 2022/12/20
https://adventofcode.com/2022/day/20

To mix the file, move each number forward or backward in the file a number of
positions equal to the value of the number being moved. The list is circular,
so moving a number off one end of the list wraps back around to the other end
as if the ends were connected.
"""
# ["1", "2", "-3", "3", "-2", "0", "4"],

__EXAMPLE__ = [
    ["2", "1", "-3", "3", "-2", "0", "4"],
    ["1", "-3", "2", "3", "-2", "0", "4"],
    ["1", "2", "3", "-2", "-3", "0", "4"],
    ["1", "2", "-2", "-3", "0", "3", "4"],
    ["1", "2", "-3", "0", "3", "4", "-2"],
    ["1", "2", "-3", "0", "3", "4", "-2"],
    ["1", "2", "-3", "4", "0", "3", "-2"],
]


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


class Node(object):
    def __init__(self, idx, data):
        self.c_idx = idx
        self.value = int(data)
        self.next = None
        self.prev = None

    def __str__(self):
        return f"""{self.value=}, {self.idx=}"""


def print_list(head: Node) -> None:
    cur = head
    tail = head.prev
    print("[", end="")
    while cur != tail:
        print(f"'{cur.value}'", end=", ")
        cur = cur.next
    else:
        print(f"'{cur.value}']")


# def main():
"""code if module is called directly"""
the_data = get_data("data_test1.txt")
# the_data = get_data("data.txt")

encrypted = []
head = None
tail = None
the_data_len = len(the_data)

# cycle through the input value by value
for idx, str_shift in enumerate(the_data):
    n = Node(idx, str_shift)
    if head is None:
        head = n
        tail = n
        n.next = head
        n.prev = tail
    else:
        n.next = head
        n.prev = tail
        tail.next = n  # n.prev.next = n
        head.prev = n  # head.prev = tail
        tail = n

    print_list(head)
    encrypted.append(n)

for node in encrypted:
    # get the number of exchanges
    target_pos = (node.c_idx + node.value) % the_data_len

    moves = target_pos - node.c_idx
    print(f"From: {node.c_idx} to {target_pos} = {moves}")

    # print(f"---\n{str_shift} moves to pos {shift}")
    # print(f"Step {idx:4}: {__EXAMPLE__[idx]}")
    # print(f"Step {idx:4}: {decrypted}")

# c0_idx = decrypted.index("0")
# c1_idx = (c0_idx + 1000) % the_data_len
# c2_idx = (c0_idx + 2000) % the_data_len
# c3_idx = (c0_idx + 3000) % the_data_len

# print(f"{c0_idx}, {c1_idx}, {c2_idx}, {c3_idx}")
# print(
#    f"{decrypted[c0_idx]}, {decrypted[c1_idx]}, {decrypted[c2_idx]}, {decrypted[c3_idx]}"
# )
# solution = int(decrypted[c1_idx]) + int(decrypted[c2_idx]) + int(decrypted[c3_idx])
# print(f"{solution=}")
# return best


# if __name__ == "__main__":
#     solution = main()
#     print(f"{solution=}")

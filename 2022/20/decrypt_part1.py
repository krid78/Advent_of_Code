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

# insert behind
# find value on target pos
# if > current pos, mode to targetpos + 1

# def main():
"""code if module is called directly"""
# the_data = get_data("data_test1.txt")
the_data = get_data("data.txt")

decrypted = the_data.copy()
the_data_len = len(the_data)

# cycle through the input value by value
for idx, str_shift in enumerate(the_data):
    # find the current position of value in target list
    d_idx = decrypted.index(str_shift)

    # get the new index in target list by shifting
    if d_idx + int(str_shift) > the_data_len:
        shift = (d_idx + int(str_shift)) % the_data_len
    else:
        shift = (d_idx + int(str_shift))

    # correct the move to zero
    #if shift == 0:
    #    shift = the_data_len - 1
    
    tmp = decrypted.pop(d_idx)
    decrypted.insert(shift, tmp)

    #print(f"---\n{str_shift} moves to pos {shift}")
    #print(f"Step {idx:4}: {__EXAMPLE__[idx]}")
    #print(f"Step {idx:4}: {decrypted}")

c0_idx = decrypted.index("0")
c1_idx = (c0_idx + 1000) % the_data_len
c2_idx = (c0_idx + 2000) % the_data_len
c3_idx = (c0_idx + 3000) % the_data_len

print(f"{c0_idx}, {c1_idx}, {c2_idx}, {c3_idx}")
print(
    f"{decrypted[c0_idx]}, {decrypted[c1_idx]}, {decrypted[c2_idx]}, {decrypted[c3_idx]}"
)
solution = int(decrypted[c1_idx]) + int(decrypted[c2_idx]) + int(decrypted[c3_idx])
print(f"{solution=}")
# return best


# if __name__ == "__main__":
#     solution = main()
#     print(f"{solution=}")

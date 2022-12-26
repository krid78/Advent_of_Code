#!/usr/bin/env python3
""" Advent of Code 2022/12/25
https://adventofcode.com/2022/day/25

Decimal | SNAFU | Solution
---------------------------------
 -2     |     = | -2 * 5^0
 -1     |     - | -1 * 5^0
  0     |     0 |  0 * 5^0
  1     |     1 |  1 * 5^0
  2     |     2 |  2 * 5^0
  3     |    1= |  1 * 5^1 - 2 * 5^0
  4     |    1- |  1 * 5^1 - 1 * 5^0
  5     |    10 |  1 * 5^1 - 0 * 5^0
  6     |    11 |  1 * 5^1 + 1 * 5^0
  7     |    12 |  1 * 5^1 + 2 * 5^0
  8     |    2= |  2 * 5^1 - 2 * 5^0
  9     |    2- |  2 * 5^1 - 1 * 5^0
 10     |    20 |  2 * 5^1 - 0 * 5^0
 15     |   1=0 |  1 * 5^2 - 2 * 5^1 - 0 * 5^0
 20     |   1-0 |  1 * 5^2 - 2 * 5^1 - 0 * 5^0
"""

snafu_table = {
    -2: "=",
    -1: "-",
    0: "0",
    1: "1",
    2: "2",
    3: "1=",
    4: "1-",
    5: "10",
    6: "11",
    7: "12",
    8: "2=",
    9: "2-",
    10: "20",
    11: "21",
    12: "22",
    13: "1==",
    14: "1=-",
    15: "1=0",
    16: "1=1",
    17: "1=2",
    18: "1-=",
    19: "1--",
    20: "1-0",
    21: "1-1",
    22: "1-2",
    23: "10=",
    24: "10-",
    25: "100",
    26: "101",
    27: "102",
    28: "11=",
    29: "11-",
    30: "110",
    31: "111",
    32: "112",
}


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def snafu2dez(snafu: str) -> int:
    """translate SNAFU to dez"""
    translate = ["=", "-", "0", "1", "2"]
    length = len(snafu)
    val = 0
    assert length > 0
    for idx, token in enumerate(snafu):
        quot = translate.index(token) - 2
        exp = length - idx - 1
        val += int(quot * 5**exp)
        # print(f"{idx=}, {token=}, {trans=}, {quot=}, {exp=} => {val=}")

    # print(f"{val=}")
    return int(val)


def dez2snafu(dez_in: int) -> str:
    """translate dez to SNAFU
    unfortunately, we do not find the exp using log"""
    # translate = ["=", "-", "0", "1", "2"]
    translate = {3: "=", 4: "-", 0: "0", 1: "1", 2: "2"}
    dez = dez_in
    snafu = ""
    snafu_l = []

    if dez == -2 or dez == -1:
        return translate[dez % 5]

    if dez == 0:
        snafu_l.insert(0, dez % 5)

    while dez > 0:
        rest = dez % 5
        snafu_l.insert(0, rest)

        dez //= 5

    # print(f"{dez_in=} => {snafu_l=}")

    if snafu_l[0] > 2:
        snafu_l.insert(0, 0)
    for i in range(len(snafu_l)):
        if snafu_l[i] >= 3:
            snafu_l[i - 1] += 1
            snafu_l[i - 1] %= 5

    for s in snafu_l:
        snafu += translate[s]

    # print(f"{dez_in=} => {snafu_l=} => {snafu=}")

    return snafu


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    # the_data = get_data("data_test2.txt")
    the_data = get_data("data.txt")

    dez = 0

    for data in the_data:
        dez += snafu2dez(data)

    solution = dez2snafu(dez)

    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

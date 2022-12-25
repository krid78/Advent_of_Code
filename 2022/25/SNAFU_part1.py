#!/usr/bin/env python3
""" Advent of Code 2022/12/25
https://adventofcode.com/2022/day/25

Decimal | SNAFU | Solution
---------------------------------
  1     |     = | -2 * 5^0
  1     |     - | -1 * 5^0
  1     |     0 |  0 * 5^0
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

import math


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

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
    """translate dez to SNAFU"""
    translate = ["=", "-", "0", "1", "2"]
    dez = dez_in
    snafu = ""
    exp = int(1 + math.log(dez_in, 5))
    while exp >= 0:
        rest = dez % 5**exp
        idx = (rest + 2) % len(translate)
        dez = dez - rest * 5**exp
        snafu = translate[idx] + snafu
        exp -= 1

    return snafu


def snafu2dezX(snafu: str) -> int:
    """translate SNAFU to dez"""

    translate = ["=", "-", "0", "1", "2"]
    length = len(snafu)
    val = 0
    assert length > 0
    for idx, token in enumerate(snafu):
        quot = translate.index(token)
        exp = length - idx - 1
        val += int(quot * 5**exp)
        # print(f"{idx=}, {token=}, {trans=}, {quot=}, {exp=} => {val=}")

    # print(f"{val=}")

    return int(val)


def dez2snafuX(dez_in: int) -> str:
    """translate dez to SNAFU"""
    translate = ["=", "-", "0", "1", "2"]
    dez = dez_in
    snafu = ""

    while dez_in > 0:
        rest = dez_in % 5
        dez_in //= 5
        idx = rest
        snafu = translate[idx] + snafu

    return snafu


# def main():
"""code if module is called directly"""
the_data = get_data("data_test1.txt")
# the_data = get_data("data_test2.txt")
# the_data = get_data("data.txt")

dez = 0
dezX = 0

for data in the_data:
    # print(f"{data} = ", end="")
    dez += snafu2dez(data)
    # print(f"{dez}")
    dezX += snafu2dezX(data)

solution = dez2snafu(dez)
solutionX = dez2snafuX(dez)

print(f"{dez} => {solution=}")
print(f"{dezX} => {solutionX=}")

# return solution
# return solutionX


# if __name__ == "__main__":
#     solution = main()
#     print(f"{solution=}")

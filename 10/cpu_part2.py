#!/usr/bin/env python3
""" Advent of Code 2022/12/10
https://adventofcode.com/2022/day/10
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def main():
    """code if module is called directly"""
    #the_data = get_data("data_test2.txt")
    the_data = get_data("data.txt")

    # value of x at cycle 0 and 1 is 1
    signal_strength = [1, 1]

    cycles_def = {
        "noop": 1,
        "addx": 2,
    }
    scope = [20, 60, 100, 140, 180, 220]

    for instruction in the_data:
        # print(f"{instruction=}")
        cycles = cycles_def[instruction.split()[0]]
        if cycles == 1:
            signal_strength.append(signal_strength[-1])
        elif cycles == 2:
            signal_strength.append(signal_strength[-1])
            signal_strength.append(signal_strength[-1] + int(instruction.split()[1]))
        else:
            return

    total = 0
    for scp in scope:
        # print(
        #     f"{scp}. cycle -> "
        #     f"X == {signal_strength[scp]}; {scp * signal_strength[scp]}"
        # )
        total += scp * signal_strength[scp]

    print(f"Part 1: {total=}")

    crt = ["."] * 40 * 6
    sprite = "###"

    for pos, pixel in enumerate(crt):
        print(f"{pixel}", end="")
        if (pos + 1) % 40 == 0:
            print()

    for cycle in range(1, len(signal_strength)):
        print(
            f"Sprite-Pos is {signal_strength[cycle]-1}, {signal_strength[cycle]}, {signal_strength[cycle]+1}"
        )
        s1, s2, s3 = (signal_strength[cycle]-1, signal_strength[cycle], signal_strength[cycle]+1)
        s1 += 40 * (cycle // 40)
        s2 += 40 * (cycle // 40)
        s3 += 40 * (cycle // 40)
        pos = cycle - 1
        print(f"Pos = {pos}; {s1}, {s2}, {s3}")
        if pos == s1:
            crt[pos] = "#"
        elif pos == s2:
            crt[pos] = "#"
        elif pos == s3:
            crt[pos] = "#"

    for pos, pixel in enumerate(crt):
        print(f"{pixel}", end="")
        if (pos + 1) % 40 == 0:
            print()


if __name__ == "__main__":
    main()

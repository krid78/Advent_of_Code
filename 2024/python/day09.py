"""Solve Advent of Code 2024, day 9

https://adventofcode.com/2024/day/9
"""

import time


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        line = in_file.readline().strip()
        content = [int(x) for x in line]
        # content = [row.rstrip() for row in in_file]

    return content


def solve_part2(the_data):
    """solve puzzle part 2"""
    solution2 = 0

    blk_list = []
    blk_idx = 0
    gap_list = []  # (start, len)
    file_list = []  # (start, len)
    for idx in range(0, len(the_data)):
        if not idx % 2:
            blk_list.extend([idx // 2] * the_data[idx])
            file_list.append((blk_idx, the_data[idx]))
        else:
            blk_list.extend(["."] * the_data[idx])
            gap_list.append((blk_idx, the_data[idx]))
        blk_idx += the_data[idx]

    # print(f"{blk_list=}")
    # print(f"{file_list=}")
    # print(f"{gap_list=}")

    file_idx = len(file_list) - 1
    while file_idx >= 0:
        file_start, file_len = file_list[file_idx]
        for gap_id in range(len(gap_list)):
            gap_start, gap_len = gap_list[gap_id]
            if gap_start < file_start and gap_len >= file_len:
                new_blk_list = blk_list[:gap_start]
                new_blk_list.extend([file_idx] * file_len)
                new_blk_list.extend(blk_list[gap_start + file_len :])
                for dot_idx in range(file_start, file_start + file_len):
                    new_blk_list[dot_idx] = "."
                gap_list[gap_id] = (gap_start + file_len, gap_len - file_len)
                blk_list = new_blk_list.copy()
                del new_blk_list
                break

        file_idx -= 1

    print("".join([str(c) for c in blk_list]))

    for pos, val in enumerate(blk_list):
        if val != ".":
            solution2 += pos * val

    return solution2


def solve_part1(the_data):
    """solve puzzle part 1"""
    solution1 = 0
    blk_list = []
    for idx in range(0, len(the_data)):
        if not idx % 2:
            blk_list.extend([idx // 2] * the_data[idx])
        else:
            blk_list.extend(["."] * the_data[idx])

    # print(f"{blk_list=}")

    front_idx = 0
    back_idx = len(blk_list) - 1
    while back_idx >= 0 and front_idx < len(blk_list) and back_idx > front_idx:
        if blk_list[front_idx] == ".":
            x = blk_list.pop(back_idx)
            assert x != "."
            blk_list[front_idx] = x
            back_idx -= 1

        while blk_list[back_idx] == "." and back_idx >= 0:
            _ = blk_list.pop(back_idx)
            back_idx -= 1

        front_idx += 1

    # print(f"{blk_list=}")

    for pos, val in enumerate(blk_list):
        solution1 += pos * val

    return solution1


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day09.data")
    # the_data = get_data("2024/data/day09.test")
    # the_data = [1, 2, 3, 4, 5]

    solution1 = solve_part1(the_data)
    solution2 = solve_part2(the_data)

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

"""Solve Advent of Code 2024, day 9

https://adventofcode.com/2024/day/9
"""

import time


def get_data(filename: str) -> list[int]:
    """
    Read input data from file and convert it into a list of integers.

    Args:
        filename (str): Path to the input file.

    Returns:
        list[int]: A list of integers parsed from the input file.
    """
    with open(filename, "r") as in_file:
        line = in_file.readline().strip()
        return [int(x) for x in line]


def create_blocks(
    the_data: list[int],
) -> tuple[list[int], list[tuple[int, int]], list[tuple[int, int]]]:
    """
    Create blocks and gaps from the input data.

    Args:
        the_data (list[int]): The input data as a list of integers.

    Returns:
        tuple: A tuple containing:
            - blk_list: A list representing the blocks and gaps.
            - file_list: List of tuples with (start, length) for files.
            - gap_list: List of tuples with (start, length) for gaps.
    """
    blk_list = []
    file_list = []
    gap_list = []
    blk_idx = 0

    for idx, val in enumerate(the_data):
        if idx % 2 == 0:
            blk_list.extend([idx // 2] * val)
            file_list.append((blk_idx, val))
        else:
            blk_list.extend(["."] * val)
            gap_list.append((blk_idx, val))
        blk_idx += val

    return blk_list, file_list, gap_list


def solve_part1(the_data: list[int]) -> int:
    """
    Solve part 1 of the puzzle.

    Args:
        the_data (list[int]): The input data as a list of integers.

    Returns:
        int: The solution for part 1.
    """
    blk_list, _, _ = create_blocks(the_data)
    front_idx, back_idx = 0, len(blk_list) - 1

    while front_idx < back_idx:
        while front_idx < len(blk_list) and blk_list[front_idx] != ".":
            front_idx += 1
        while back_idx >= 0 and blk_list[back_idx] == ".":
            back_idx -= 1
        if front_idx < back_idx:
            blk_list[front_idx], blk_list[back_idx] = blk_list[back_idx], "."

    return sum(pos * val for pos, val in enumerate(blk_list) if val != ".")


def solve_part2(the_data: list[int]) -> int:
    """
    Solve part 2 of the puzzle.

    Args:
        the_data (list[int]): The input data as a list of integers.

    Returns:
        int: The solution for part 2.
    """
    blk_list, file_list, gap_list = create_blocks(the_data)

    for file_idx in range(len(file_list) - 1, -1, -1):
        file_start, file_len = file_list[file_idx]

        for gap_idx, (gap_start, gap_len) in enumerate(gap_list):
            if gap_start < file_start and gap_len >= file_len:
                blk_list[gap_start : gap_start + file_len] = [file_idx] * file_len
                blk_list[file_start : file_start + file_len] = ["."] * file_len
                gap_list[gap_idx] = (gap_start + file_len, gap_len - file_len)
                break

    return sum(pos * val for pos, val in enumerate(blk_list) if val != ".")


def solve() -> tuple[int, int]:
    """
    Solve the puzzle.

    Returns:
        tuple[int, int]: Solutions for part 1 and part 2.
    """
    the_data = get_data("2024/data/day09.data")
    # the_data = get_data("2024/data/day09.test")
    solution1 = solve_part1(the_data)
    solution2 = solve_part2(the_data)
    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

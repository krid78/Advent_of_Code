import time
from collections import deque


def get_data(filename: str) -> list[int]:
    """
    Return file contents as a list of integers.
    """
    with open(filename, "r") as in_file:
        line = in_file.readline().strip()
        return [int(x) for x in line.split()]


def solve_stone(stone: int, iterations: int, cache: dict) -> int:
    """Solve one stone."""

    # at the end of the recursion, one stone is left
    if iterations == 0:
        ret = 1
    elif (stone, iterations) in cache:
        # we already know, how this stone works
        ret = cache[(stone, iterations)]
    elif stone == 0:
        ret = solve_stone(1, iterations - 1, cache)
    elif len(str(stone)) % 2 == 0:
        sstone = str(stone)
        lstone = len(sstone) // 2
        left = int(sstone[:lstone])
        right = int(sstone[lstone:])
        ret = solve_stone(left, iterations - 1, cache) + solve_stone(
            right, iterations - 1, cache
        )
    else:
        ret = solve_stone(stone * 2024, iterations - 1, cache)

    cache[(stone, iterations)] = ret

    return ret


def solve(the_data: int, iterations: int) -> int:
    """solve the puzzle."""
    stone_dict = {}

    stones = 0
    for stone in the_data:
        stones += solve_stone(stone, iterations, stone_dict)

    return stones


if __name__ == "__main__":
    time_start = time.perf_counter()
    the_data = get_data("2024/data/day11.data")
    # the_data = get_data("2024/data/day11.test")
    solution1 = solve(the_data, iterations=25)
    solution2 = solve(the_data, iterations=75)  # Set iterations to 75 for part 2
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

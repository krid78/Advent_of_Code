import time
from collections import deque


def get_data(filename: str) -> list[int]:
    """
    Return file contents as a list of integers.
    """
    with open(filename, "r") as in_file:
        line = in_file.readline().strip()
        return [int(x) for x in line.split()]


def solve(the_data, iterations: int) -> int:
    """
    Solve the puzzle.

    Args:
        iterations (int): Number of iterations to perform.

    Returns:
        tuple[int, int]: The solutions for part 1 and part 2.
    """

    # Use a deque for faster insertion and removal
    part1 = deque(the_data)

    for _ in range(iterations):
        new_elements = deque()
        while part1:
            value = part1.popleft()  # Remove from the front
            if value == 0:
                new_elements.append(1)
            else:
                sval = str(value)
                lval = len(sval)
                if lval % 2 == 0:  # Even-length number
                    lval //= 2
                    new_elements.append(int(sval[:lval]))
                    new_elements.append(int(sval[lval:]))
                else:  # Odd-length number
                    new_elements.append(value * 2024)

        # Update part1 with new_elements
        part1 = new_elements

    return len(part1)


if __name__ == "__main__":
    time_start = time.perf_counter()
    the_data = get_data("2024/data/day11.data")
    # the_data = get_data("2024/data/day11.test")
    solution1 = solve(the_data, iterations=25)
    solution2 = solve(the_data, iterations=75)  # Set iterations to 75 for part 2
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

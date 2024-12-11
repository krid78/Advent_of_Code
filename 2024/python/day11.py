import time
from collections import deque


def get_data(filename: str) -> list[int]:
    """
    Return file contents as a list of integers.
    """
    with open(filename, "r") as in_file:
        line = in_file.readline().strip()
        return [int(x) for x in line.split()]


def process_chunk(chunk: deque, iterations: int) -> deque:
    """
    Process a chunk of data for the given number of iterations.

    Args:
        chunk (deque): The current chunk of data.
        iterations (int): Number of iterations to perform on this chunk.

    Returns:
        deque: The processed data.
    """
    for _ in range(iterations):
        new_elements = deque()
        while chunk:
            value = chunk.popleft()
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
        chunk = new_elements
    return chunk


def solve(the_data, iterations: int, chunk_size: int = 1000) -> int:
    """
    Solve the puzzle.

    Args:
        the_data (list[int]): Initial data.
        iterations (int): Number of iterations to perform.
        chunk_size (int): Size of each chunk to process at once.

    Returns:
        int: The final size of the processed data.
    """
    total_size = 0

    # Split data into chunks
    for i in range(0, len(the_data), chunk_size):
        chunk = deque(the_data[i : i + chunk_size])
        print(f"Processing chunk {i // chunk_size + 1}...")
        chunk = process_chunk(chunk, iterations)
        total_size += len(chunk)

    return total_size


if __name__ == "__main__":
    time_start = time.perf_counter()
    # the_data = get_data("2024/data/day11.data")
    the_data = get_data("2024/data/day11.test")

    print("Processing part 1 (25 iterations)...")
    solution1 = solve(the_data, iterations=25, chunk_size=100)

    print("Processing part 2 (75 iterations)...")
    solution2 = solve(the_data, iterations=75, chunk_size=100)

    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

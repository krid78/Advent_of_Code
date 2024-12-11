import time
from collections import deque
from concurrent.futures import ProcessPoolExecutor


def get_data(filename: str) -> list[int]:
    """
    Return file contents as a list of integers.
    """
    with open(filename, "r") as in_file:
        line = in_file.readline().strip()
        return [int(x) for x in line.split()]


def process_chunk(chunk: list[int], iterations: int) -> int:
    """
    Process a chunk of data for the given number of iterations.

    Args:
        chunk (list[int]): The current chunk of data.
        iterations (int): Number of iterations to perform on this chunk.

    Returns:
        int: The size of the processed chunk.
    """
    chunk = deque(chunk)
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
    return len(chunk)


def solve(the_data: list[int], iterations: int, chunk_size: int = 1000) -> int:
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
    chunks = [the_data[i : i + chunk_size] for i in range(0, len(the_data), chunk_size)]

    # Parallel processing
    with ProcessPoolExecutor() as executor:
        for i, chunk_size in enumerate(
            executor.map(process_chunk, chunks, [iterations] * len(chunks))
        ):
            print(f"Chunk {i + 1} processed, size: {chunk_size}")
            total_size += chunk_size

    return total_size


if __name__ == "__main__":
    time_start = time.perf_counter()
    the_data = get_data("2024/data/day11.data")
    # the_data = get_data("2024/data/day11.test")

    print("Processing part 1 (25 iterations)...")
    solution1 = solve(the_data, iterations=25, chunk_size=10)

    print("Processing part 2 (75 iterations)...")
    solution2 = solve(the_data, iterations=75, chunk_size=10)

    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

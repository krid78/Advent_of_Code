"""Solve Advent of Code 2024, day 18

https://adventofcode.com/2024/day/18
"""

import heapq
import time


def get_data(filename: str) -> list[tuple[int, int]]:
    """
    Parse file contents into a list of coordinate tuples.

    Args:
        filename (str): Path to the input file.

    Returns:
        list[tuple[int, int]]: A list of (x, y) coordinates.
    """
    coordinates = []
    with open(filename, "r") as in_file:
        for line in in_file:
            if line.strip():  # Skip empty lines
                x, y = map(int, line.strip().split(","))
                coordinates.append((x, y))

    return coordinates


def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
    """
    Calculate the Manhattan distance between two points.

    Args:
        a (tuple[int, int]): The first point (x1, y1).
        b (tuple[int, int]): The second point (x2, y2).

    Returns:
        int: The Manhattan distance between the points.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve_part1(
    walls: set[tuple[int, int]], lx: int, ly: int
) -> tuple[int, list[tuple[int, int]]]:
    """
    Find the shortest path from (0, 0) to (lx, ly) using A*.

    Args:
        walls (set[tuple[int, int]]): Set of wall coordinates.
        lx (int): Target x-dimension.
        ly (int): Target y-dimension.

    Returns:
        tuple[int, list[tuple[int, int]]]: The length of the shortest path and the path itself.
    """
    start = (0, 0)
    goal = (lx, ly)

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Priority queue for A*
    open_set = []
    heapq.heappush(open_set, (0, start))

    # Cost from start to each node
    g_score = {start: 0}

    # Track visited nodes and paths
    came_from = {}

    while open_set:
        current_cost, current = heapq.heappop(open_set)

        # Check if we reached the goal
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return g_score[goal], path

        # Explore neighbors
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if (
                neighbor in walls
                or neighbor[0] < 0
                or neighbor[1] < 0
                or neighbor[0] > lx
                or neighbor[1] > ly
            ):
                continue

            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = tentative_g_score
                came_from[neighbor] = current
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return -1, []  # No path found


def find_blocking_bricks(
    the_data: list[tuple[int, int]],
    walls: set[tuple[int, int]],
    path: list[tuple[int, int]],
    lx: int,
    ly: int,
):
    current_block = len(walls)
    for x, y in the_data[current_block:]:
        if (x, y) in path:
            print(f"({x=},{y=}) is in path")
            walls.add((x, y))
            res, path = solve_part1(walls, lx, ly)
            if res < 0:
                return (x, y)
        else:
            walls.add((x, y))


def visualize_grid(
    walls: set[tuple[int, int]], path: list[tuple[int, int]], lx: int, ly: int
) -> None:
    """
    Visualize the grid with walls, free spaces, and the path.

    Args:
        walls (set[tuple[int, int]]): Set of wall coordinates.
        path (list[tuple[int, int]]): List of coordinates representing the path.
        lx (int): Grid width.
        ly (int): Grid height.
    """
    grid = [["." for _ in range(lx + 1)] for _ in range(ly + 1)]

    for x, y in walls:
        grid[y][x] = "#"

    for x, y in path:
        if (x, y) not in walls:
            grid[y][x] = "o"

    grid[0][0] = "S"
    grid[ly][lx] = "E"

    for row in grid:
        print("".join(row))


def solve(test=False):
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    # Read the data from the file

    if test:
        the_data = get_data("2024/data/day18.test")
        walls = set(the_data[:12])
        lx, ly = 6, 6
    else:
        the_data = get_data("2024/data/day18.data")
        walls = set(the_data[:1024])
        lx, ly = 70, 70

    time_start = time.perf_counter()
    solution1, path = solve_part1(walls, lx, ly)
    print(f"Part 1 solved in {time.perf_counter()-time_start:.5f} Sec.")

    if test:
        print(f"Shortest path length: {solution1}")
        print("Visualization:")
        visualize_grid(walls, path, lx, ly)
        print("#" * 50)

    time_start = time.perf_counter()
    solution2 = find_blocking_bricks(the_data, walls, path, lx, ly)
    print(f"Part 2 solved in {time.perf_counter()-time_start:.5f} Sec.")

    if test:
        visualize_grid(walls, path, lx, ly)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve(False)
    print(f"{solution1=} | {solution2=}")

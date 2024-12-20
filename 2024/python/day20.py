"""Solve Advent of Code 2024, day 20

https://adventofcode.com/2024/day/20
"""

import time
import heapq

# Bewegungsrichtungen (oben, rechts, unten, links)
__DIRECTIONS__ = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_data(filename: str) -> list[str]:
    """
    Return file contents as list of strings.

    Args:
        filename (str): Path to the input file.

    Returns:
        list[str]: List of strings representing the map.
    """
    with open(filename, "r") as in_file:
        return [row.strip() for row in in_file]


def parse_data(
    content: list[str],
) -> tuple[set[tuple[int, int]], tuple[int, int], tuple[int, int]]:
    """
    Parse the labyrinth data.

    Args:
        content (list[str]): List of strings representing the labyrinth.

    Returns:
        tuple[set[tuple], tuple, tuple]: A set of walls, the start position, and the goal position.
    """
    walls = set()
    start, goal = None, None

    map_dim = (len(content), len(content[0]))

    for r, row in enumerate(content):
        for c, char in enumerate(row):
            if char == "#":
                walls.add((r, c))
            elif char == "S":
                start = (r, c)
            elif char == "E":
                goal = (r, c)

    if start is None or goal is None:
        raise ValueError("Start or goal position is missing.")

    return walls, start, goal, map_dim


def draw_map(
    walls: set[tuple[int, int]],
    start: tuple[int, int],
    goal: tuple[int, int],
    map_dim: tuple[int, int],
    path: list[tuple[int, int]],
    cheat: tuple[tuple[int, int], tuple[int, int]],
):

    path_marker = {(-1, 0): "^", (0, 1): ">", (1, 0): "v", (0, -1): "<"}
    grid = [[" " for _ in range(map_dim[1])] for _ in range(map_dim[0])]
    for r, c in walls:
        grid[r][c] = "#"
    for i in range(len(path) - 1):
        current = path[i]
        next_pos = path[i + 1]
        marker = path_marker[(next_pos[0] - current[0], next_pos[1] - current[1])]
        grid[current[0]][current[1]] = marker

    grid[start[0]][start[1]] = "S"
    grid[goal[0]][goal[1]] = "E"

    grid[cheat[0]][cheat[1]] = "O"

    for row in grid:
        print("".join(row).strip())


def find_shortest_path(
    walls: set[tuple[int, int]], start: tuple[int, int], goal: tuple[int, int]
) -> tuple[int, list[tuple[int, int]]]:
    """
    Find the shortest path from start to goal using Dijkstra's algorithm.

    Args:
        walls (set[tuple[int, int]]): Set of wall positions.
        start (tuple[int, int]): Start position.
        goal (tuple[int, int]): Goal position.

    Returns:
        tuple[int, list[tuple[int, int]]]: The cost of the shortest path and the path itself.
    """
    pq = []  # Priority queue: (cost, position, path)
    heapq.heappush(pq, (0, start, [start]))
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return cost, path

        for dr, dc in __DIRECTIONS__:
            neighbor = (current[0] + dr, current[1] + dc)

            if neighbor in walls or neighbor in visited:
                continue

            heapq.heappush(pq, (cost + 1, neighbor, path + [neighbor]))

    return float("inf"), []  # No path found


def find_cheating_spots(
    walls: set[tuple[int, int]],
    path: list[tuple[int, int]],
) -> dict:
    """
    Identify potential cheating spots along the path.

    Args:
        walls (set[tuple[int, int]]): Set of wall positions.
        path (list[tuple[int, int]]): Shortest path from start to goal.
        map_dim (tuple[int, int]): Number of rows and columns in the map.
        start (tuple[int, int]): Start position.
        goal (tuple[int, int]): Goal position.

    Returns:
        set[tuple[tuple[int, int], tuple[int, int]]]: Set of wall positions to remove for potential shortcuts.
    """

    cheating_spots = {}
    # pos -> wall -> path

    for rp, cp in path:
        for dr, dc in __DIRECTIONS__:
            wall = (rp + dr, cp + dc)
            next_pos = (rp + 2 * dr, cp + 2 * dc)

            if wall in walls and wall not in cheating_spots and next_pos in path:
                cheating_spots[wall] = [(rp, cp), next_pos]

    return cheating_spots


def find_cheating_spots2(
    walls: set[tuple[int, int]],
    path: list[tuple[int, int]],
) -> dict:
    """
    Identify potential cheating spots along the path.

    Args:
        walls (set[tuple[int, int]]): Set of wall positions.
        path (list[tuple[int, int]]): Shortest path from start to goal.
        map_dim (tuple[int, int]): Number of rows and columns in the map.
        start (tuple[int, int]): Start position.
        goal (tuple[int, int]): Goal position.

    Returns:
        set[tuple[tuple[int, int], tuple[int, int]]]: Set of wall positions to remove for potential shortcuts.
    """

    cheating_spots = {}
    # pos -> wall -> path

    for rs, cs in path[1:-1]:
        for dr, dc in __DIRECTIONS__:
            wall = (rs + dr, cs + dc)
            next_pos = (rs + 2 * dr, cs + 2 * dc)

            if wall in walls and wall not in cheating_spots and next_pos in path:
                cheating_spots[wall] = [(rs, cs), next_pos]

    return cheating_spots

def solve_part1(
    walls: set[tuple[int, int]],
    map_dim,
    start: tuple[int, int],
    goal: tuple[int, int],
    cheating_saves: int = 100,
) -> int:
    """
    Solve part 1 by finding good cheating spots.

    Args:
        walls (set[tuple[int, int]]): Set of wall positions.
        start (tuple[int, int]): Start position.
        goal (tuple[int, int]): Goal position.
        cheating_saves (int): Minimum cost savings for a cheating spot.

    Returns:
        int: Number of good cheating spots.
    """
    base_cost, way = find_shortest_path(walls, start, goal)

    if base_cost == float("inf"):
        return 0  # No path found

    print(f"{base_cost=}")

    # Identify cheating spots (walls along the way)
    cheating_spots = find_cheating_spots(walls, way)
    print(f"Possible Cheating spots: {len(cheating_spots)}")
    
    good_cheating = {}

    for cutoff_start, cutoff_end in cheating_spots.values():

        # Recalculate shortest path
        # csp_cost, cut_way = find_shortest_path(walls, cutoff_start, cutoff_end)
        co_start = way.index(cutoff_start)
        co_end = way.index(cutoff_end)
        cheat_saving = co_end - co_start - 2

        # Restore the wall(s)
        # walls.add(csp)

        # cheat_saving = base_cost - csp_cost
        # print("="*10 + f" Removing {csp}, and a way from {cut_off[0]} to {cut_off[1]}, saving {csp_cost=} leaving costs of {cheat_saving=}")
        # draw_map(walls, start, goal, map_dim, new_way, csp)

        if cheat_saving >= cheating_saves:
            good_cheating[cheat_saving] = good_cheating.setdefault(cheat_saving, 0) + 1

    # for k in sorted(good_cheating):
    #     print(f"There are {good_cheating[k]:3} cheats that save {k:3} picoseconds.")

    return sum(v for k, v in good_cheating.items() if k >= cheating_saves)


def solve(test: bool = False):
    """
    Solve the puzzle.

    Args:
        test (bool): Whether to use test data or production data.

    Returns:
        tuple[int, int]: Solutions for part 1 and part 2.
    """
    solution1 = 0
    solution2 = 0

    if test:
        cheating_saves1 = 2
        cheating_saves2 = 50
        the_data = get_data("2024/data/day20.test")
    else:
        cheating_saves1 = cheating_saves2 = 100
        the_data = get_data("2024/data/day20.data")

    walls, start, goal, map_dim = parse_data(the_data)

    time_start = time.perf_counter()
    solution1 = solve_part1(walls, map_dim, start, goal, cheating_saves1)
    print(f"Part 1 solved in {time.perf_counter()-time_start:.5f} Sec.")

    # time_start = time.perf_counter()
    # solution2 = solve_part1(walls, map_dim, start, goal, cheating_saves2)
    # print(f"Part 1 solved in {time.perf_counter()-time_start:.5f} Sec.")

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve(False)
    print(f"{solution1=} | {solution2=}")

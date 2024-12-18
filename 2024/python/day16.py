from collections import deque

# Bewegungsrichtungen (oben, rechts, unten, links)
__DIRECTIONS__ = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
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

    return walls, start, goal


def bfs_find_all_paths(walls, start, goal):
    """
    Find all paths from start to goal in a maze using BFS.

    Args:
        walls (set[tuple[int, int]]): Set of wall positions in the maze.
        start (tuple[int, int]): Start position (row, col).
        goal (tuple[int, int]): Goal position (row, col).

    Returns:
        tuple[int, list[list[tuple[int, int]]]]: Minimal cost and all paths with minimal cost.
    """
    queue = deque([(start, 1, [start], 0)])  # (current position, direction, path, cost)
    minimal_cost = float("inf")
    minimal_paths = []

    while queue:
        current_pos, current_dir, path, current_cost = queue.popleft()

        # Ziel erreicht
        if current_pos == goal:
            if current_cost < minimal_cost:
                minimal_cost = current_cost
                minimal_paths = [path]
            elif current_cost == minimal_cost:
                minimal_paths.append(path)
            continue

        r, c = current_pos
        for new_dir, (dr, dc) in enumerate(__DIRECTIONS__):
            nr, nc = r + dr, c + dc

            # Wände ignorieren
            if (nr, nc) in walls or (nr, nc) in path:
                continue

            # Bewegungskosten berechnen
            turn_cost = 1000 if new_dir != current_dir else 0
            move_cost = 1
            new_cost = current_cost + turn_cost + move_cost

            # Neuen Zustand in die Warteschlange legen
            queue.append(((nr, nc), new_dir, path + [(nr, nc)], new_cost))

    return minimal_cost, minimal_paths


def solve():
    """Solve the puzzle."""
    the_data = get_data("2024/data/day16.data")
    # the_data = get_data("2024/data/day16.0.test")
    # the_data = get_data("2024/data/day16.1.test")

    walls, start, goal = parse_data(the_data)

    # Minimalen Pfad und alle minimalen Wege berechnen
    min_cost, minimal_paths = bfs_find_all_paths(walls, start, goal)

    # Anzahl der minimalen Pfade
    num_minimal_paths = len(minimal_paths)

    # Ausgabe der minimalen Pfade
    print(f"Minimal cost: {min_cost}")
    print(f"Number of minimal paths: {num_minimal_paths}")
    tiles = set()
    for i, path in enumerate(minimal_paths, 1):
        # print(f"Path {i}: {path}")
        tiles.update(path)

    print(f"Anzahl Tiles: {len(tiles)}")
    return min_cost, num_minimal_paths


if __name__ == "__main__":
    solve()

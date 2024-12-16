import time
import heapq

# Bewegungsrichtungen (oben, rechts, unten, links)
__DIRECTIONS__ = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        return [row.strip() for row in in_file]


def parse_data(content: list[str]) -> tuple[set[tuple], tuple, tuple]:
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


def dijkstra(walls: set[tuple], start: tuple[int, int], goal: tuple[int, int]) -> int:
    """
    Use Dijkstra's algorithm to find the shortest path from start to goal.

    Args:
        walls (set[tuple]): Set of wall positions in the labyrinth.
        start (tuple[int, int]): Starting position (row, col).
        goal (tuple[int, int]): Goal position (row, col).

    Returns:
        int: The minimum cost to reach the goal.
    """
    # Priority queue: (current cost, position, direction)
    pq = []
    heapq.heappush(pq, (0, start, 1))  # Start with direction "1" (rechts)

    # Distance table: (position, direction) -> cost
    dist = {}

    while pq:
        current_cost, (r, c), direction = heapq.heappop(pq)

        # Ziel erreicht
        if (r, c) == goal:
            return current_cost

        # Wenn der Zustand bereits mit geringeren Kosten besucht wurde, überspringen
        if ((r, c), direction) in dist and dist[((r, c), direction)] <= current_cost:
            continue
        dist[((r, c), direction)] = current_cost

        # Nachbarn prüfen
        for turn, (dr, dc) in enumerate(__DIRECTIONS__):
            new_dir = turn
            nr, nc = r + dr, c + dc

            if (nr, nc) in walls:
                continue  # Wände ignorieren

            # Drehkosten berechnen
            turn_cost = 1000 if new_dir != direction else 0
            move_cost = 1  # Schritt kostet immer 1

            # Gesamtkosten für diesen Schritt
            next_cost = current_cost + move_cost + turn_cost

            # In die Warteschlange einfügen
            heapq.heappush(pq, (next_cost, (nr, nc), new_dir))

    return -1  # Kein Weg gefunden


def heuristic(position: tuple[int, int], goal: tuple[int, int]) -> int:
    """
    Manhattan distance heuristic for A*.

    Args:
        position (tuple[int, int]): Current position.
        goal (tuple[int, int]): Goal position.

    Returns:
        int: Estimated cost to reach the goal.
    """
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


def a_star(walls: set[tuple], start: tuple[int, int], goal: tuple[int, int]) -> int:
    """
    Use A* algorithm to find the shortest path from start to goal.

    Args:
        walls (set[tuple]): Set of wall positions in the labyrinth.
        start (tuple[int, int]): Starting position (row, col).
        goal (tuple[int, int]): Goal position (row, col).

    Returns:
        int: The minimum cost to reach the goal.
    """
    # Priority queue: (total cost, current cost, position, direction)
    pq = []
    heapq.heappush(pq, (0, 0, start, 1))  # Start with direction "1" (rechts)

    # Visited set to track visited states: (position, direction)
    visited = set()

    while pq:
        total_cost, current_cost, (r, c), direction = heapq.heappop(pq)

        # Ziel erreicht
        if (r, c) == goal:
            return current_cost

        # Zustand als besucht markieren
        if ((r, c), direction) in visited:
            continue
        visited.add(((r, c), direction))

        # Nachbarn prüfen
        for turn, (dr, dc) in enumerate(__DIRECTIONS__):
            new_dir = turn
            nr, nc = r + dr, c + dc

            if (nr, nc) in walls:
                continue  # Wände ignorieren

            # Drehkosten berechnen
            turn_cost = 1000 if new_dir != direction else 0
            move_cost = 1  # Schritt kostet immer 1

            # Gesamtkosten für diesen Schritt
            next_cost = current_cost + move_cost + turn_cost
            estimated_cost = next_cost + heuristic((nr, nc), goal)

            # In die Warteschlange einfügen
            heapq.heappush(pq, (estimated_cost, next_cost, (nr, nc), new_dir))

    return -1  # Kein Weg gefunden


def find_all_paths(walls, start, goal):
    """
    Find all minimal-cost paths from start to goal in a maze.

    Args:
        walls (set[tuple[int, int]]): Set of wall positions in the maze.
        start (tuple[int, int]): Start position (row, col).
        goal (tuple[int, int]): Goal position (row, col).

    Returns:
        dict[int, set[tuple[int, int]]]: A dictionary with costs as keys and the set of all unique
                                         tiles covered by minimal-cost paths as values.
    """
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    stack = [(start, 1, [start], 0)]  # (current position, direction, path, cost)
    all_paths = {}

    while stack:
        current_pos, current_dir, path, current_cost = stack.pop()

        # Ziel erreicht, aktuellen Pfad speichern
        if current_pos == goal:
            all_paths.setdefault(current_cost, set()).update(path)
            continue

        r, c = current_pos
        for new_dir, (dr, dc) in enumerate(directions):
            new_pos = (r + dr, c + dc)

            # Wände ignorieren
            if new_pos in walls or new_pos in path:
                continue

            # Bewegungskosten berechnen
            turn_cost = 1000 if new_dir != current_dir else 0
            move_cost = 1
            new_cost = current_cost + turn_cost + move_cost

            # Frühzeitiger Abbruch, falls Kosten unnötig hoch
            if new_cost > min(all_paths.keys(), default=float("inf")):
                continue

            # Neuen Zustand auf den Stapel legen
            stack.append((new_pos, new_dir, path + [new_pos], new_cost))

    return all_paths


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day16.data")
    # the_data = get_data("2024/data/day16.0.test") # 7036 | 45
    # the_data = get_data("2024/data/day16.1.test") # 11048 | 64
    walls, start, goal = parse_data(the_data)

    time_start = time.perf_counter()
    solution1 = dijkstra(walls, start, goal)
    print(f"Solved Part 1 in {time.perf_counter()-time_start:.5f} Sec.")

    time_start = time.perf_counter()
    all_paths = find_all_paths(walls, start, goal)
    min_cost = min(all_paths.keys())
    solution2 = len(all_paths[min_cost])
    print(f"Solved Part 2 in {time.perf_counter()-time_start:.5f} Sec.")

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
    print(f"{solution1=} | {solution2=}")

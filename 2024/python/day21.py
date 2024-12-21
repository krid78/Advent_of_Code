"""Solve Advent of Code 2024, day 21

https://adventofcode.com/2024/day/21

+---+---+---+    +-----+-----+-----+
| 7 | 8 | 9 | -> | 3,2 | 3,1 | 3,0 |
+---+---+---+    +-----+-----+-----+
| 4 | 5 | 6 | -> | 2,2 | 2,1 | 2,0 |
+---+---+---+    +-----+-----+-----+
| 1 | 2 | 3 | -> | 1,2 | 1,1 | 1,0 |
+---+---+---+    +-----+-----+-----+
    | 0 | A | -> | 0,2 | 0,1 | 0,0 |
    +---+---+    +-----+-----+-----+

    +---+---+ -> +-----+-----+-----+ -> +-------+-------+-------+
    | ^ | A | -> | 1,2 | 1,1 | 1,0 | -> |       |  1, 0 |  0, 0 |
+---+---+---+ -> +-----+-----+-----+ -> +-------+-------+-------+
| < | v | > | -> | 0,2 | 0,1 | 0,0 | -> |  0, 1 | -1, 0 |  0,-1 |
+---+---+---+ -> +-----+-----+-----+ -> +-------+-------+-------+


All start at "A"

P2: <vA <A A >>^A vA A <^A >A <v<A >>^A vA ^A <vA >^A <v<A >^A >A A vA ^A <v<A >A >^A A A vA <^A >A
P1:   v  < <    A  > >   ^  A    <    A  >  A   v   A    <   ^  A A  >  A    <  v   A A A  >   ^  A
P0:             <           A         ^     A       >           ^ ^     A           v v v         A
NP:                         0               2                           9                         A

P2: <vA <A A >>^A vA A <^A >A <v<A >>^A vA ^A <vA >^A <v<A >^A >A A vA ^A <v<A >A >^A A A vA <^A >A
NP:                         0               2                           9                         A


Move Left: <vA<AA
Move Right: vA
"""

import time

# Bewegungsrichtungen (oben, rechts, unten, links)
__DIRECTIONS__ = [(-1, 0), (0, 1), (1, 0), (0, -1)]
__DIRECTION_MAP__ = {
    (1, 0): "^",
    (0, -1): ">",
    (-1, 0): "v",
    (0, 1): "<",
}


def get_num_coordinates():
    """
    Define the mapping of keys to coordinates on the grid.

    Returns:
        dict: Mapping of keys to their respective coordinates (row, column).
    """
    return {
        "7": (3, 2),
        "8": (3, 1),
        "9": (3, 0),
        "4": (2, 2),
        "5": (2, 1),
        "6": (2, 0),
        "1": (1, 2),
        "2": (1, 1),
        "3": (1, 0),
        "0": (0, 1),
        "A": (0, 0),
    }


def get_arrow_coordinates():
    """
    Define the mapping of keys to coordinates on the grid.

    Returns:
        dict: Mapping of keys to their respective coordinates (row, column).
    """
    return {
        "A": (1, 0),
        "^": (1, 1),
        ">": (0, 0),
        "v": (0, 1),
        "<": (0, 2),
    }


def calculate_path(start: str, end: str, coord_map: dict) -> list[str]:
    """
    Calculate the path from start to end as a sequence of directions.

    Args:
        start (str): Starting key on the grid.
        end (str): Ending key on the grid.
        coord_map (dict): Mapping of keys to coordinates.

    Returns:
        list[str]: List of directions (`<`, `^`, `v`, `>`) and `A` for keys.
    """
    path = []
    start_coord = coord_map[start]
    end_coord = coord_map[end]

    # Calculate row movements
    while start_coord[0] != end_coord[0]:
        dr = 1 if end_coord[0] > start_coord[0] else -1
        path.append(__DIRECTION_MAP__[(dr, 0)])
        start_coord = (start_coord[0] + dr, start_coord[1])

    # Calculate column movements
    while start_coord[1] != end_coord[1]:
        dc = 1 if end_coord[1] > start_coord[1] else -1
        path.append(__DIRECTION_MAP__[(0, dc)])
        start_coord = (start_coord[0], start_coord[1] + dc)

    # Append `A` for the target key
    path.append("A")

    return path


def calculate_full_path(sequence: str) -> list[str]:
    """
    Calculate the full path for a sequence of keys.

    Args:
        sequence (str): A string of keys (e.g., "029A").

    Returns:
        list[str]: Full list of directions (`<`, `^`, `v`, `>`) and `A` for keys.
    """
    coord_map = get_num_coordinates()
    full_path = []

    for i in range(len(sequence) - 1):
        start = sequence[i]
        end = sequence[i + 1]
        full_path.extend(calculate_path(start, end, coord_map))

    return full_path


# Example usage
if __name__ == "__main__":
    sequence = "029A"
    start_time = time.perf_counter()
    path = calculate_full_path("A" + sequence)
    print(f"Path for sequence {sequence}: {' '.join(path)}")
    print(f"Computed in {time.perf_counter() - start_time:.5f} seconds.")

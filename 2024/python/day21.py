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

    +---+---+ -> +-----+-----+-----+
    | ^ | A | -> | 1,2 | 1,1 | 1,0 |
+---+---+---+ -> +-----+-----+-----+
| < | v | > | -> | 0,2 | 0,1 | 0,0 |
+---+---+---+ -> +-----+-----+-----+

All start at "A"

"""

import time

# Bewegungsrichtungen (runter, links, hoch, rechts)
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
    Define the mapping of keys to coordinates on the arrow grid.

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
    
    def move_vertical(cc, tc):
        # Move vertically
        while cc[0] != tc[0]:
            dr = 1 if tc[0] > cc[0] else -1
            path.append(__DIRECTION_MAP__[(dr, 0)])
            cc = (cc[0] + dr, cc[1])
            assert cc != (0,2)
        return cc

    def move_horizontal(cc, tc):
        # Move horizontally
        while cc[1] != tc[1]:
            dc = 1 if tc[1] > cc[1] else -1
            path.append(__DIRECTION_MAP__[(0, dc)])
            cc = (cc[0], cc[1] + dc)
            assert cc != (0,2)
        return cc
    
    path = []
    start_coord = coord_map[start]
    end_coord = coord_map[end]

    if start_coord[0] < 1:
        start_coord = move_vertical(start_coord, end_coord)
        start_coord = move_horizontal(start_coord, end_coord)
    elif end_coord[0] < 1:
        start_coord = move_horizontal(start_coord, end_coord)
        start_coord = move_vertical(start_coord, end_coord)
    else:     
        start_coord = move_vertical(start_coord, end_coord)
        start_coord = move_horizontal(start_coord, end_coord)

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


def map_to_arrow_path(sequence: list[str]) -> list[str]:
    """
    Map a sequence of movements and `A` to arrow coordinates.

    Args:
        sequence (list[str]): A sequence of directions (`<`, `^`, `v`, `>`) and `A`.

    Returns:
        list[str]: Transformed sequence in the arrow coordinate system.
    """

    def move_vertical(cc, tc):
        # Move vertically
        while cc[0] != tc[0]:
            dr = 1 if tc[0] > cc[0] else -1
            arrow_path.append("^" if dr > 0 else "v")
            cc = (cc[0] + dr, cc[1])
            assert cc != (1,2)
        return cc

    def move_horizontal(cc, tc):
        # Move horizontally
        while cc[1] != tc[1]:
            dc = 1 if tc[1] > cc[1] else -1
            arrow_path.append("<" if dc > 0 else ">")
            cc = (cc[0], cc[1] + dc)
            assert cc != (1,2)
        return cc

    arrow_coords = get_arrow_coordinates()
    arrow_path = []
    current_coord = (1, 0)  # Start at "A"

    for item in sequence:
        target_coord = arrow_coords[item]

        #if current_coord == (0,2) and target_coord==(1,0):
        #    arrow_path.append(">")
        #    arrow_path.append("^")
        #    arrow_path.append(">")
        #    current_coord = target_coord
        if current_coord[0] > target_coord[0]:
            current_coord = move_vertical(current_coord, target_coord)
            current_coord = move_horizontal(current_coord, target_coord)
        else:
            current_coord = move_horizontal(current_coord, target_coord)
            current_coord = move_vertical(current_coord, target_coord)

        # Append the symbol
        arrow_path.append("A")

    return arrow_path


# Example usage
if __name__ == "__main__":
    # sequences = ["140A", "143A", "349A", "582A", "964A"]
    sequences = ["029A", "980A", "179A", "456A", "379A"]
    solution1 = 0
    start_time = time.perf_counter()
    for sequence in sequences:
        path = calculate_full_path("A" + sequence)
        print(f"Path for sequence {sequence}: {''.join(path)}")
        arrow_path1 = map_to_arrow_path(path)
        print(f"Path for sequence {sequence}: {''.join(arrow_path1)}")
        arrow_path2 = map_to_arrow_path(arrow_path1)
        print(f"Path for sequence {sequence}: {''.join(arrow_path2)}")
        solution1 += int(sequence[:-1]) * len(arrow_path2)
        print(f"{len(arrow_path2)} * {int(sequence[:-1])}")

    print(
        f"Solution 1: {solution1} Computed in {time.perf_counter() - start_time:.5f} seconds."
    )

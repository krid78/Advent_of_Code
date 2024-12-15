"""Solve Advent of Code 2024, day 15

https://adventofcode.com/2024/day/15
"""

import time


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    move_start = content.index("")
    global map_rows
    map_rows = move_start
    global map_cols
    map_cols = len(content[0])

    return content[:move_start], move_start, "".join(content[move_start:])


def get_data_part1(map_data):
    walls = set()
    boxes = set()

    for r in range(len(map_data)):
        for c in range(len(map_data[0])):
            if map_data[r][c] == "#":
                walls.add((r, c))
            elif map_data[r][c] == "O":
                boxes.add((r, c))
            elif map_data[r][c] == "@":
                bot_pos = (r, c)

    return walls, boxes, bot_pos


def get_data_part2(map_data):
    walls = set()
    boxes = set()

    global map_cols
    map_cols = len(map_data[0]) * 2

    for r in range(len(map_data)):
        for c in range(len(map_data[0])):
            if map_data[r][c] == "#":
                walls.add((r, c * 2))
                walls.add((r, c * 2 + 1))
            elif map_data[r][c] == "O":
                boxes.add((r, c * 2))
                boxes.add((r, c * 2 + 1))
            elif map_data[r][c] == "@":
                bot_pos = (r, c * 2)

    return walls, boxes, bot_pos


def print_map(walls, boxes, bot_pos):
    grid = [["." for _ in range(map_cols)] for _ in range(map_rows)]
    for r, c in walls:
        grid[r][c] = "#"
    for r, c in boxes:
        assert grid[r][c] == "."
        grid[r][c] = "O"

    assert grid[bot_pos[0]][bot_pos[1]] == "."
    grid[bot_pos[0]][bot_pos[1]] = "@"

    for row in grid:
        print("".join(row).strip())


def print_map2(walls, boxes, bot_pos):
    grid = [["." for _ in range(map_cols)] for _ in range(map_rows)]
    for r, c in sorted(walls):
        grid[r][c] = "#"
        # grid[r][c + 1] = "#"
    for r, c in sorted(boxes):
        assert grid[r][c] == "."
        if grid[r][c-1] in "]#.":
            grid[r][c] = "["
        else:
            grid[r][c] = "]"

    assert grid[bot_pos[0]][bot_pos[1]] == "."
    grid[bot_pos[0]][bot_pos[1]] = "@"

    for row in grid:
        print("".join(row).strip())


def move_boxes(
    walls: set[tuple], boxes: set[tuple], br: int, bc: int, dr: int, dc: int
):

    # find boxes to move
    boxes_to_move = []

    while (br, bc) in boxes:
        boxes_to_move.append((br, bc))
        br += dr
        bc += dc
    else:
        if (br, bc) in walls:
            # print(f"{boxes_to_move} end on wall ({br}, {bc})")
            return False

    # update box positions
    for br, bc in boxes_to_move[::-1]:
        boxes.remove((br, bc))
        br += dr
        bc += dc
        boxes.add((br, bc))

    # return true, if position is free
    return True


def move_boxes2(
    walls: set[tuple], boxes: set[tuple], br: int, bc: int, dr: int, dc: int
):

    # simple horizontal move
    if dr == 0:
        return move_boxes(walls, boxes, br, bc, dr, dc)

    # komplex vertical move
    # seams not to work with my current idea

    # return true, if position is free
    return True


def calc_distances(boxes):
    gps = [100 * r + c for r, c in boxes]
    return sum(gps)


def solve_part1(walls, boxes, bot_pos, moves):
    directions = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    r, c = bot_pos
    for move in moves:
        dr, dc = directions[move]
        nr, nc = r + dr, c + dc
        if (nr, nc) in walls:
            continue
        elif (nr, nc) in boxes:
            if not move_boxes(walls, boxes, nr, nc, dr, dc):
                continue
        else:
            pass

        r, c = (nr, nc)
        # print_map(walls, boxes, (r, c))

    return calc_distances(boxes)


def solve_part2(walls, boxes, bot_pos, moves):
    directions = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    r, c = bot_pos
    for move in moves:
        dr, dc = directions[move]
        nr, nc = r + dr, c + dc
        if (nr, nc) in walls:
            continue
        elif (nr, nc) in boxes:
            if not move_boxes2(walls, boxes, nr, nc, dr, dc):
                continue
        else:
            pass

        r, c = (nr, nc)
        # print_map2(walls, boxes, (r, c))

    return calc_distances(boxes)


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    the_data, move_start, moves = get_data("2024/data/day15.data")
    # the_data, move_start, moves = get_data("2024/data/day15.test")
    # the_data, move_start, moves = get_data("2024/data/day15s.test")
    # the_data, move_start, moves = get_data("2024/data/day15w.test")

    walls, boxes, bot_pos = get_data_part1(the_data)
    solution1 = solve_part1(walls, boxes, bot_pos, moves)

    walls, boxes, bot_pos = get_data_part2(the_data)
    print_map2(walls, boxes, bot_pos)
    solution2 = solve_part2(walls, boxes, bot_pos, moves)

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve()
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

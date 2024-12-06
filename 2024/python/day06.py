"""Solve Advent of Code 2024, day 6

https://adventofcode.com/2024/day/6
"""

__DIRECTIONS__ = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
]


def get_data(filename: str) -> list[str]:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def look_right(the_data, vis, obs, pos):
    """look right, if we find a spot"""
    row, col = pos[:2]
    dr, dc = __DIRECTIONS__[drc := ((pos[2] + 1) % 4)]

    while 0 <= row < len(the_data) and 0 <= col < len(the_data[0]):
        row += dr
        col += dc
        if (row, col) in obs:
            row -= dr
            col -= dc
            break
    else:
        return False

    if (row, col, drc) in vis:
        # print(f"Found: {row}, {col}, {drc}")
        return True

    return False


def solve_part2(the_data: list[str], obstructions, start) -> int:
    """Solve part 1"""

    row, col = start[:2]
    dr, dc = __DIRECTIONS__[direction := start[2]]
    visited = [start]
    blocks = set()

    while 0 < row < len(the_data) - 1 and 0 < col < len(the_data[0]) - 1:
        row += dr
        col += dc
        if (row, col) in obstructions:
            row -= dr
            col -= dc
            direction = (direction + 1) % 4
            dr, dc = __DIRECTIONS__[direction]
        elif (row, col, direction) not in visited:
            the_data[row] = the_data[row][:col] + "X" + the_data[row][col + 1 :]
            visited.append((row, col, direction))
        else:
            pass

        if look_right(the_data, visited, obstructions, (row, col, direction)):
            # print(f"{(row+dr, col+dc, direction)}")
            blocks.add((row + dr, col + dc, direction))

    # print("\n".join(the_data))

    return len(blocks)


def solve_part1(the_data: list[str], obstructions, start, direction) -> int:
    """Solve part 1"""

    row, col = start
    dr, dc = __DIRECTIONS__[direction]
    visited = [start]

    while 0 < row < len(the_data) - 1 and 0 < col < len(the_data[0]) - 1:
        row += dr
        col += dc
        if (row, col) in obstructions:
            row -= dr
            col -= dc
            direction = (direction + 1) % 4
            dr, dc = __DIRECTIONS__[direction]
        elif (row, col) not in visited:
            the_data[row] = the_data[row][:col] + "X" + the_data[row][col + 1 :]
            visited.append((row, col))
        else:
            pass

    # print("\n".join(the_data))

    return len(visited)


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day06.data")
    # the_data = get_data("2024/data/day06.test")

    obstructions = []

    for row, rdata in enumerate(the_data):
        for col, cdata in enumerate(rdata):
            if cdata == "#":
                obstructions.append((row, col))
            elif cdata == "^":
                start = (row, col, 0)
            elif cdata == ">":
                start = (row, col, 1)
            elif cdata == "v":
                start = (row, col, 2)
            elif cdata == "<":
                start = (row, col, 3)
            else:
                pass

    # print(f"{start=}, {obstructions=}")

    solution1 = solve_part1(the_data, obstructions, (start[:2]), start[2])
    solution2 = solve_part2(the_data, obstructions, start)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
    print(f"{solution1=} | {solution2=}")

#!/usr/bin/env python3
""" Advent of Code 2022/12/22
https://adventofcode.com/2022/day/22

https://de.wikipedia.org/wiki/Spielw%C3%BCrfel

One is next to 2, 3, 4, 5; never to 6
Six is next to 2, 3, 4, 5; never to 1
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


# def main():
"""code if module is called directly"""
# the_data = get_data("data_test1.txt")
the_data = get_data("data.txt")

moves = the_data.pop()
print(moves)

valid_coordinates = []  # [[(row, col), ...], ...]
stone_coordinates = []  # [(row, col), ]

for row, data in enumerate(the_data[:-1]):
    valid_coordinates.append([])
    for col, val in enumerate(data):
        if val == ".":
            valid_coordinates[row].append((row, col))
        elif val == "#":
            stone_coordinates.append((row, col))
        else:
            pass


# .......R(0)....D(1).....L(2).....U(3)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
head = 0
pos = valid_coordinates[0][0]
print(f"Start Pos: {pos}")

while moves:
    spl = min(moves.find("L"), moves.find("R"))
    if spl < 0:
        spl = max(moves.find("L"), moves.find("R"))

    if spl >= 0:
        move, turn, moves = moves.partition(moves[spl])
    else:
        move, turn, moves = moves, None, None

    move = int(move)
    # print(f"Move {move:3} Steps from {pos=} to {dirs[head]}")
    #    if (row, col) == (194, 35):
    #        print("Debug-In")

    # first, move
    while move > 0:
        row, col = pos
        d_row, d_col = dirs[head]
        new_row = row + d_row
        new_col = col + d_col

        col_max = max(valid_coordinates[row])
        col_min = min(valid_coordinates[row])

        if new_row < len(valid_coordinates) and (
            (new_row, new_col) in valid_coordinates[new_row]
            or (new_row, new_col) in stone_coordinates
        ):
            print(f"{(new_row, new_col)}: Valid or Stone")
            pass  # this case only prevents the else
        elif d_col > 0 and new_col > col_max[1]:
            new_col = col_min[1]
            # print(f"{(new_row, new_col)}: Valid or Stone")
        elif d_col < 0 and new_col < col_min[1]:
            new_col = col_max[1]
            # print(f"{(new_row, new_col)}: Valid or Stone")
        elif d_row != 0:
            new_row = (new_row - d_row) % len(valid_coordinates)
            while (new_row, new_col) in valid_coordinates[new_row] or (
                new_row,
                new_col,
            ) in stone_coordinates:
                new_row = (new_row - d_row) % len(valid_coordinates)
            new_row = (new_row + d_row) % len(valid_coordinates)
            # print(f"{(new_row, new_col)} wrapped y-bound")
        else:
            print(f"No rule for {(new_row, new_col)}")

        if (new_row, new_col) in stone_coordinates:
            # print(f"{(new_row, new_col)}: Stone")
            new_row, new_col = row, col
            # print(f"{(new_row, new_col)}: Stone-Reset")

        pos = (new_row, new_col)
        move -= 1

    print(f"New valid position: {pos}")

    # then turn
    if turn == "R":
        head = (head + 1) % 4
    elif turn == "L":
        head = (head - 1) % 4

print(f"Position: {pos}, Heading {head}")
solution = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + head
print(f"{solution=}")
# return solution


# if __name__ == "__main__":
#     solution = main()
#     print(f"{solution=}")

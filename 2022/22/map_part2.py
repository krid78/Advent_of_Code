#!/usr/bin/env python3
""" Advent of Code 2022/12/22
https://adventofcode.com/2022/day/22

for a more general solution:
  - peaces are 50x50
  - width // 50
  - height // 50
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def get_moves(the_data: list) -> list:
    """return the moves, shorten data in place
    Remember: python hands lists as pointer"""
    moves = the_data.pop()
    # drop the empty line
    the_data.pop()
    # print(moves)
    return moves


def extract_valid_coordinates(the_data: list) -> tuple:
    """return two lists of valid coordinates
    use (row, col) format (y, x)"""
    valid = []  # [[(row, col), ...], ...]
    stone = []  # [(row, col), ]

    for row, data in enumerate(the_data):
        valid.append([])
        for col, val in enumerate(data):
            if val == ".":
                valid[row].append((row, col))
            elif val == "#":
                stone.append((row, col))
            else:
                pass

    return valid, stone


def next_move(moves):
    """get the next move and turn"""
    spl = min(moves.find("L"), moves.find("R"))
    if spl < 0:
        spl = max(moves.find("L"), moves.find("R"))

    if spl >= 0:
        move, turn, moves = moves.partition(moves[spl])
    else:
        move, turn, moves = moves, None, None

    return move, turn, moves


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    moves = get_moves(the_data)

    valid_coordinates, stone_coordinates = extract_valid_coordinates(the_data)

    # .......R(0)....D(1).....L(2).....U(3)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    head = 0
    pos = valid_coordinates[0][0]
    print(f"Start Pos: {pos}")

    while moves:
        move, turn, moves = next_move(moves)
        move = int(move)
        # print(f"Move {move:3} Steps from {pos=} to {dirs[head]}")
        #    if (row, col) == (194, 35):
        #        print("Debug-In")

        # first, move
        while move > 0:
            row, col = pos
            new_head = head
            d_row, d_col = dirs[head]
            new_row = row + d_row
            new_col = col + d_col

            col_max = max(valid_coordinates[row])
            col_min = min(valid_coordinates[row])

            if (
                new_row >= 0
                and new_row < len(valid_coordinates)
                and (
                    (new_row, new_col) in valid_coordinates[new_row]
                    or (new_row, new_col) in stone_coordinates
                )
            ):
                pass
            elif d_col > 0 and new_col > col_max[1]:  # overflow right
                if 0 <= new_row < 50:  # 2 to 5
                    # 2 to 5 and 5 to 2 are quite equal TODO: combine
                    new_row = 149 - new_row
                    new_col = 99
                    new_head = (head + 2) % 4
                elif 100 <= new_row < 150:  # 5 to 2
                    # 2 to 5 and 5 to 2 are quite equal TODO: combine
                    new_row = 149 - new_row
                    new_col = 149
                    new_head = (head + 2) % 4
                elif 50 <= new_row < 100:  # 3 to 2
                    # 3 to 2 or 6 to 5 are quite equal TODO: combine
                    new_col = new_row + 50  # 3 to 2
                    new_row = (50 * (new_row // 50)) - 1
                    new_head = 3  # "up"
                elif 150 <= new_row < 200:  # 6 to 5
                    # 3 to 2 or 6 to 5 are quite equal TODO: combine
                    new_col = new_row - 100  # 6 to 5
                    new_row = (50 * (new_row // 50)) - 1
                    new_head = 3  # "up"
            elif d_col < 0 and new_col < col_min[1]:
                if 0 <= new_row < 50:  # 4 to 1
                    new_row = 149 - new_row  # (new_row + 149) % 200
                    new_col = 0  # min(valid_coordinates[new_row])[1]
                    new_head = (head + 2) % 4
                elif 100 <= new_row < 150:  # 1 to 4
                    new_row = 149 - new_row  # (new_row + 149) % 200
                    new_col = 50  # min(valid_coordinates[new_row])[1]
                    new_head = (head + 2) % 4
                elif 50 <= new_row < 100:  # 3 to 4
                    new_col = new_row - 50  # 3 to 4
                    new_row = 100
                    new_head = 1  # "down"
                elif 150 <= new_row < 200:  # 6 to 1
                    new_col = new_row - 100  # 6 to 1
                    new_row = 0
                    new_head = 1  # "down"
            elif d_row < 0 and new_row < 0 and 50 <= new_col < 100:  # 1 to 6
                # 1 to 6 and 4 to 3 are equal TODO: combine
                new_row = new_col + 100
                new_col = 0
                new_head = 0  # "right"
            elif d_row < 0 and new_row < 100 and 0 <= new_col < 50:  # 4 to 3
                new_row = new_col + 50
                new_col = 50
                new_head = 0  # "right"
            elif d_row > 0 and new_row >= 50 and 100 <= new_col <= col_max[1]:  # 2 to 3
                # 2 to 3 and 5 to 6 are equal TODO: combine
                new_row = new_col - 50
                new_col = 99
                new_head = 2
            elif d_row > 0 and new_row >= 150 and 50 <= new_col < 100:  # 5 to 6
                new_row = new_col + 100
                new_col = 49
                new_head = 2
            elif d_row != 0 and (new_row < 0 or new_row > 199):  # 2 to 6 or 6 to 2
                new_col = new_col + 100 * dirs[head][0]
                new_row = new_row % 200  # 199 for -1 and 0 for 200
                new_head = head
            else:
                print(f"No rule for {(new_row, new_col)} coming from {pos}")

            if (new_row, new_col) in stone_coordinates:
                # print(f"{(new_row, new_col)}: Stone")
                new_row, new_col, new_head = row, col, head
                break
                # print(f"{(new_row, new_col)}: Stone-Reset")

            pos = (new_row, new_col)
            head = new_head
            move -= 1

        # print(f"New valid position: {pos}")

        # then turn
        if turn == "R":
            head = (head + 1) % 4
        elif turn == "L":
            head = (head - 1) % 4

    print(f"Position: {pos}, Heading {head}")
    solution = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + head
    print(f"{solution=} (134076)")
    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

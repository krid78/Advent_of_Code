#!/usr/bin/env python3
""" Advent of Code 2022/12/21
https://adventofcode.com/2022/day/21
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def print_map(a_map: list, offsets: list) -> None:
    """print the map"""
    for idx, line in enumerate(a_map):
        print(" " * offsets[idx], end="")
        print("".join(line))


# def main():
"""code if module is called directly"""
the_data = get_data("data_test1.txt")
# the_data = get_data("data.txt")

moves = the_data.pop()
print(moves)

the_map = []
map_offsets = []

for data in the_data:
    if data == "":
        continue
    offset = min(data.find("."), data.find("#"))
    if offset < 0:
        offset = max(data.find("."), data.find("#"))

    the_map.append(list(data.strip()))
    map_offsets.append(offset)

print_map(the_map, map_offsets)

# .....R(0)...D(1).....L(2).......U(3)
dirs=[(1,0), (0, 1), (-1, 0), (0, -1)]
head = 0
pos = (map_offsets[0], 0)

while moves:
    spl = min(moves.find('L'), moves.find('R'))
    if spl < 0:
        spl = max(moves.find('L'), moves.find('R'))

    if spl >= 0:
        move, turn, moves = moves.partition(moves[spl])
    else:
        move, turn, moves = moves, None, None

    move = int(move)
    print(f"Move {move} Steps from {pos=} to {dirs[head]}")    

    # first, move
    while move > 0:
        x, y = pos
        dx, dy = dirs[head]
        x = (x + dx) % len(the_map[y])
        y = (y + dy)
        move -= 1

    # then turn
    if turn == 'R':
        head = (head + 1) % 4
    elif turn == 'L':
        head = (head - 1) % 4
    

# return solution


# if __name__ == "__main__":
#     solution = main()
#     print(f"{solution=}")

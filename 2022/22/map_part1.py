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


# def main():
"""code if module is called directly"""
# the_data = get_data("data_test1.txt")
the_data = get_data("data.txt")

moves = the_data.pop()
# print(moves)

the_map = []
offsets = []

for data in the_data:
    if data == "":
        continue
    offset = min(data.find("."), data.find("#"))
    if offset < 0:
        offset = max(data.find("."), data.find("#"))

    the_map.append(data)
    offsets.append(offset)

# for line in the_map:
#     print(line)

# .....R(0)...D(1).....L(2).......U(3)
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
head = 0
pos = (offsets[0], 0)

while moves:
    spl = min(moves.find("L"), moves.find("R"))
    if spl < 0:
        spl = max(moves.find("L"), moves.find("R"))

    if spl >= 0:
        move, turn, moves = moves.partition(moves[spl])
    else:
        move, turn, moves = moves, None, None

    move = int(move)
    print(f"Move {move} Steps from {pos=} to {dirs[head]}")

    # first, move
    while move > 0:
        x, y = pos
        if x == 75 and y == 148:
            print("Foo")
        dx, dy = dirs[head]
        new_x = x + dx
        new_y = y + dy
        if dx != 0:
            if new_x >= len(the_map[new_y]):
                new_x = offsets[new_y]
            if new_x < offsets[new_y]:
                new_x = len(the_map[new_y]) - 1
            if the_map[new_y][new_x] != ".":
                new_x = x
        if dy != 0:
            # End of map, go back
            if new_y < 0:
                new_y -= dy
                while len(the_map[new_y]) >= new_x and the_map[new_y][new_x] != " ":
                    new_y = (new_y - dy) % len(the_map)
                new_y += dy
            if new_y >= len(the_map):
                new_y -= dy
                while len(the_map[new_y]) >= new_x and offsets[new_y] < new_x:
                    new_y = (new_y - dy) % len(the_map)
                new_y += dy
            # End of overlapping right space
            if new_x >= len(the_map[new_y]):
                new_y -= dy
                while len(the_map[new_y]) >= new_x and the_map[new_y][new_x] != " ":
                    new_y = (new_y - dy) % len(the_map)
                new_y += dy
            # End of overlapping left space
            if the_map[new_y][new_x] == " ":
                new_y -= dy
                while the_map[new_y][new_x] != " ":
                    new_y = (new_y - dy) % len(the_map)
                new_y += dy

            if the_map[new_y][new_x] != ".":
                new_y = y

        pos = (new_x, new_y)
        move -= 1

    print(pos)

    # then turn
    if turn == "R":
        head = (head + 1) % 4
    elif turn == "L":
        head = (head - 1) % 4

print(f"Position: {pos}, Heading {head}")
solution = 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + head
print(f"{solution=}")
# return solution


# if __name__ == "__main__":
#     solution = main()
#     print(f"{solution=}")

#!/usr/bin/env python3
""" Advent of Code 2022/12/14
https://adventofcode.com/2022/day/14
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def draw(surface):
    """draw the pyramid"""
    min_x = 500
    max_x = 0
    min_y = 0
    max_y = 0
    for x, y in surface:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(surface.get((x, y), "."), end="")
        print()


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    surface = {}

    for data in the_data:
        path = [tuple(map(int, t.split(","))) for t in data.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            dx = x2 - x1
            dy = y2 - y1

            if dx != 0:
                dx = (dx) / abs(dx)

            if dy != 0:
                dy = (dy) / abs(dy)

            surface[(x1, y1)] = "#"
            while (x1, y1) != (x2, y2):
                x1 += int(dx)
                y1 += int(dy)
                surface[(x1, y1)] = "#"

    max_y = 0
    for _, y in surface:
        max_y = max(max_y, y)

    sand_y = 0
    sand_x = 0
    count = 0
    while (sand_x, sand_y) != (500, 0):
        sand_x, sand_y = (500, 0)
        blocked = False
        count += 1
        while blocked is False and sand_y < (max_y + 1):
            for dx, dy in ((0, 1), (-1, 1), (1, 1)):
                blocked = True
                if surface.get((sand_x + dx, sand_y + dy)) is None:
                    blocked = False
                    sand_x += dx
                    sand_y += dy
                    break

            if blocked is True:
                surface[(sand_x, sand_y)] = "o"
                print(f"Stopped at obstacle {(sand_x, sand_y)}")
            elif sand_y == max_y + 1:
                surface[(sand_x, sand_y)] = "o"
                surface[(sand_x, sand_y + 1)] = "#"
                print(f"Stopped at bottom {(sand_x, sand_y)}")

    # draw(surface)
    return count


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

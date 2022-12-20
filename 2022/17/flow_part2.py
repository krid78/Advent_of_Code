#!/usr/bin/env python3
""" Advent of Code 2022/12/17
https://adventofcode.com/2022/day/17

We need a occupancy map, holding the occupied spaces in the tower
One approach is using binary data (& for collision detection, | for placing)
The resulting list of numbers is easy to handle. This is a perfect approach for
C (memcmp, binary operations), but also an idea for python.
An other approach is a set holding x,y-Coordinates. Here the set handles
collisions and placement. Finding repetitions is also possible.
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = in_file.readline().strip()

    return content


def print_rock(coords: list, base=0) -> None:
    """print a rock"""
    length, height = 0, 0
    shape = []
    coords.sort()
    for x, y in coords:
        length = max(length, x + 1)
        height = max(height, y + 1)

    shape = [["." for _ in range(length)] for _ in range(height)]
    for x, y in coords:
        shape[y][x] = "#"

    for line in range(height, base, -1):
        print("".join(shape[line - 1]))


def tower_cache(cache, key, r_cnt, t_height):
    """"""
    if key in cache:
        # number of rocks handled per interval
        rc_interval = r_cnt - cache[key]["rc"]
        # height we get per interval
        h_interval = t_height - cache[key]["th"]
        remaining_rocks = 1e12 - r_cnt
        cache[key]["rc"] = r_cnt
        cache[key]["th"] = t_height
        cache[key]["hit"] += 1
        hit_count = cache[key]["hit"]
        if remaining_rocks % rc_interval == 0:
            print(
                f"Cache hit after {r_cnt=} rocks\n"
                f"  {t_height=}, key={key}\n"
                f"  {rc_interval=}, {h_interval=}\n"
                f"  {(remaining_rocks // r_cnt)=}, "
                f"{(remaining_rocks % r_cnt)=}\n"
                f"  {(remaining_rocks // rc_interval)=}, "
                f"{(remaining_rocks % rc_interval)=}\n"
                f"  Cache: {cache[key]}\n"
                f"  Next Hit at {(r_cnt) * 2}"
            )
            return t_height + h_interval * (remaining_rocks // rc_interval)
    else:
        cache[key] = {
            "rc": r_cnt,
            "th": t_height,
            "hit": 0,
        }

    return None


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    rock_shapes = [
        {
            "coords": [(0, 0), (1, 0), (2, 0), (3, 0)],
            "width": 4,
            "height": 1,
        },
        {
            "coords": [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
            "width": 3,
            "height": 3,
        },
        {
            "coords": [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
            "width": 3,
            "height": 3,
        },
        {
            "coords": [(0, 0), (0, 1), (0, 2), (0, 3)],
            "width": 1,
            "height": 4,
        },
        {
            "coords": [(0, 0), (1, 0), (0, 1), (1, 1)],
            "width": 2,
            "height": 2,
        },
    ]

    tower = set()
    cache = {}
    tower_height = 0
    shift_cnt = 0
    rock_count = 0

    while rock_count < 1e12:
        if tc := tower_cache(
            cache, (rock_count % 5, shift_cnt), rock_count, tower_height
        ):
            tower_height = tc
            break
        rock = rock_shapes[rock_count % 5]
        # print(rock)
        # print_rock(list(tower | set(rock_pos)), 1)
        rx = 2
        ry = tower_height + 3 + 1
        rock_pos = [(rx + x, ry + y) for x, y in rock["coords"]]
        while True:
            shift = ord(the_data[shift_cnt]) - 61
            shift_cnt = (shift_cnt + 1) % len(the_data)
            next_rock_pos = [(x + shift, y) for x, y in rock_pos]
            valid = all(-1 < x < 7 and y > 0 for x, y in next_rock_pos)
            if not (tower & set(next_rock_pos)) and valid:
                rock_pos = next_rock_pos
            next_rock_pos = [(x, y - 1) for x, y in rock_pos]
            valid = all(-1 < x < 7 and y > 0 for x, y in next_rock_pos)
            if not (tower & set(next_rock_pos)) and valid:
                rock_pos = next_rock_pos
            else:
                break

        tower |= set(rock_pos)
        tower_height = max(tower_height, max([y for _, y in rock_pos]))
        # print_rock(list(tower), 1)
        rock_count += 1

    # print("-----")
    # print(f"{tower=}")
    # print_rock(list(tower), 1)
    # print(f"{rock_count=}, {tower_height=}")
    return tower_height


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

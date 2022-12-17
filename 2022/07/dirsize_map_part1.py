#!/usr/bin/env python3
""" Advent of Code 2022/12/07
https://adventofcode.com/2022/day/7
"""


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [line.strip() for line in in_file]

    return content


def get_size(dir_map, name):
    """get size of dir"""
    if len(dir_map[name]["sub_dirs"]) == 0:
        return dir_map[name]["size"]

    size = dir_map[name]["size"]
    for name in dir_map[name]["sub_dirs"]:
        size += get_size(dir_map, name)

    return size


def main():
    the_data = get_data("data_test.txt")
    # the_data = get_data("data.txt")

    dir_map = {}
    cur_dir = None

    for line in the_data:
        match line.split():
            # cd into
            case [_, cmd, name] if cmd == "cd" and name != "..":
                dir_map[name] = {
                    "parent": cur_dir,
                    "size": 0,
                    "sub_dirs": [],
                }
                cur_dir = name
            # cd one up
            case [_, cmd, name] if cmd == "cd" and name == "..":
                if dir_map[cur_dir]["parent"] is not None:
                    cur_dir = dir_map[cur_dir]["parent"]
            # sub dir
            case [cmd, name] if cmd == "dir":
                dir_map[cur_dir]["sub_dirs"].append(name)
            # a file
            case [size, name] if size != "$" and size != "dir":
                dir_map[cur_dir]["size"] += int(size)
            case _:
                pass

    print(f"{dir_map=}")
    total = 0
    for a_dir in dir_map:
        size = get_size(dir_map, a_dir)
        print(f"{a_dir}: {size}")
        if size < 100000:
            total += size

    print(f"{total=}")


if __name__ == "__main__":
    main()

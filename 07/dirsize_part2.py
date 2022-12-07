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


class File(object):
    """represent a file (Name, Size)"""

    def __init__(self, name, size) -> None:
        self.__name = name
        self.__size = size

    def get_size(self) -> int:
        """return size of file"""
        return self.__size


class Dir(object):
    """Represent a Directory of Dir and File"""

    size = 0

    def __init__(self, name, parent) -> None:
        self.parent = parent
        if parent is not None:
            parent.add_dir(self)
        self.name = name
        self.__dirs = []
        self.__files = []

    def add_dir(self, dir):
        """Add a dir to my list"""
        self.__dirs.append(dir)

    def add_file(self, file):
        """Add a dir to my list"""
        self.__files.append(file)

    def get_size(self) -> int:
        """return size of dir and subdirs"""
        size = 0
        for dir in self.__dirs:
            size += dir.get_size()

        for fl in self.__files:
            size += fl.get_size()

        return size


def main():
    # the_data = get_data("data_test.txt")
    the_data = get_data("data.txt")
    dir_list = []
    cur_dir = None

    for line in the_data:
        match line.split():
            case [_, cmd, name] if cmd == "cd" and name == "..":
                if cur_dir.parent is not None:
                    cur_dir = cur_dir.parent
            case [_, cmd, name] if cmd == "cd" and name != "..":
                cur_dir = Dir(name, cur_dir)
                dir_list.append(cur_dir)
            case [size, name] if size != "$" and size != "dir":
                cur_dir.add_file(File(name, int(size)))
            case _:
                pass

    print(f"{dir_list=}")
    free_space = 70000000 - dir_list[0].get_size()
    needed_space = 30000000 - free_space
    print(f"{needed_space=}")

    candidates = []
    for a_dir in dir_list:
        # print(f"{a_dir.name}: {a_dir.get_size()}")
        if a_dir.get_size() >= needed_space:
            candidates.append(a_dir.get_size())

    candidates.sort()
    print(f"{candidates=}")


if __name__ == "__main__":
    main()

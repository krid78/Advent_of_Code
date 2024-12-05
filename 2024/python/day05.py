"""Solve Advent of Code 2024, day 5

https://adventofcode.com/2024/day/5
"""


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    the_data = get_data("2024/data/day05.data")
    # the_data = get_data("2024/data/day05.test")

    upd_start = the_data.index("")

    page_map = {}
    for idx in range(upd_start):
        pre, post = map(int, the_data[idx].split("|"))

        if pre not in page_map:
            page_map[pre] = []
        page_map[pre].append(post)

    for line in the_data[upd_start + 1 :]:
        l = [x for x in map(int, line.split(","))]
        correct = True
        for li, lv in enumerate(l):
            left = set(l[:li])
            try:
                right = set(page_map[lv])
            except KeyError:
                right = {}

            if set(left) & set(right):
                correct = False
                break

        if correct:
            print(f"{l=}")
            print(f"{l[len(l)//2]}")
            solution1 += l[len(l) // 2]

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
    print(f"{solution1=} | {solution2=}")

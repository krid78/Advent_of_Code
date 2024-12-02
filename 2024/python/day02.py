"""Solve Advent of Code 2024, day 2

https://adventofcode.com/2024/day/2
"""


def get_data(filename: str) -> list:
    """Return file contents as list"""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def check_report(report):
    """check the given report"""
    res = False
    print(f"{report=}", end="")
    if 0 < (int(report[0]) - int(report[1])) < 4:
        safe = {1, 2, 3}
    elif -4 < (int(report[0]) - int(report[1])) < 0:
        safe = {-1, -2, -3}
    else:
        print(" has no safe set")
        return res, 0

    for idx in range(1, len(report) - 1):
        check = int(report[idx]) - int(report[idx + 1])
        if check not in safe:
            print(f" is not safe ({report[idx]=}, {report[idx+1]=}, {check=}, {safe=})")
            break
    else:
        print(" is safe")
        res = True

    return res, idx


def solve1(the_data):
    """Solve puzzle part 1"""
    solution = 0
    for line in the_data:
        report = line.split()
        res, _ = check_report(report)
        if res:
            solution += 1

        # print(f"{report=}", end="")
        # if 0 < (int(report[0]) - int(report[1])) < 4:
        #    safe = {1, 2, 3}
        # elif -4 < (int(report[0]) - int(report[1])) < 0:
        #    safe = {-1, -2, -3}
        # else:
        #    print(" has no safe set")
        #    continue
        # for idx in range(1, len(report) - 1):
        #    check = int(report[idx]) - int(report[idx + 1])
        #    if check not in safe:
        #        print(
        #            f" is not safe ({report[idx]=}, {report[idx+1]=}, {check=}, {safe=})"
        #        )
        #        break
        # else:
        #    print(" is safe")
        #    solution += 1

    return solution


def solve2(the_data):
    """Solve puzzle part 1"""
    solution = 0

    # check()
    # drop self, check()
    # drop next, check()
    for line in the_data:
        print("========")
        report = line.split()

        res, idx = check_report(report)

        if not res:
            print("report=", end="")
            print(report[:idx] + report[idx + 1 :], end="")
            print(" --> retry")
            res, _ = check_report(report[:idx] + report[idx + 1 :])

        if not res:
            print("report=", end="")
            print(report[: idx + 1] + report[idx + 2 :], end="")
            print(" --> retry")
            res, _ = check_report(report[: idx + 1] + report[idx + 2 :])

        if res:
            solution += 1
            print(f"{solution=}")

    return solution


def solve():
    """Solve the puzzle"""
    solution1 = 0
    solution2 = 0

    the_data = get_data(
        "/home/dkrieste/Dokumente/Develop/advent-of-code/2024/data/day02.data"
    )
    # the_data = get_data(
    #     "/home/dkrieste/Dokumente/Develop/advent-of-code/2024/data/day02.test"
    # )

    # solution1 = solve1(the_data)
    solution2 = solve2(the_data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
    print(f"{solution1=} | {solution2=}")

"""Solve Advent of Code 2024, day 21

https://adventofcode.com/2024/day/21

+---+---+---+    +-----+-----+-----+
| 7 | 8 | 9 | -> | 3,2 | 3,1 | 3,0 |
+---+---+---+    +-----+-----+-----+
| 4 | 5 | 6 | -> | 2,2 | 2,1 | 2,0 |
+---+---+---+    +-----+-----+-----+
| 1 | 2 | 3 | -> | 1,2 | 1,1 | 1,0 |
+---+---+---+    +-----+-----+-----+
    | 0 | A | -> |     | 0,1 | 0,0 |
    +---+---+    +-----+-----+-----+

    +---+---+ -> +-----+-----+-----+
    | ^ | A | -> |     | 0,1 | 0,0 |
+---+---+---+ -> +-----+-----+-----+
| < | v | > | -> | 1,2 | 1,1 | 1,0 |
+---+---+---+ -> +-----+-----+-----+


All start at "A"

P2: <vA <A A >>^A vA A <^A >A <v<A >>^A vA ^A <vA >^A <v<A >^A >A A vA ^A <v<A >A >^A A A vA <^A >A
P1:   v  < <    A  > >   ^  A    <    A  >  A   v   A    <   ^  A A  >  A    <  v   A A A  >   ^  A
P0:             <           A         ^     A       >           ^ ^     A           v v v         A
NP:                         0               2                           9                         A

P2: <vA <A A >>^A vA A <^A >A <v<A >>^A vA ^A <vA >^A <v<A >^A >A A vA ^A <v<A >A >^A A A vA <^A >A
NP:                         0               2                           9                         A


Move Left: <vA<AA
Move Right: vA
"""

import time


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


class Pad(object):
    def __init__(self):
        self.pos = "A"
        self.pad = None
        self.type = "Pad"

    def __repr__(self):
        return f"{self.pos}"

    def __str__(self):
        return f"{self.type}@{self.pos}"


class NumPad(Pad):
    def __init__(self):
        super().__init__()
        self.pad = {
            "A": (0, 0),
            "0": (0, 1),
            "3": (1, 0),
            "2": (1, 1),
            "1": (1, 2),
            "6": (2, 0),
            "5": (2, 1),
            "4": (2, 2),
            "9": (3, 0),
            "8": (3, 1),
            "7": (3, 2),
        }
        self.type = "NumPad"

    def activate(self):
        return self.move_to("A")

    def move_to(self, target: str = "A") -> tuple[int, int]:
        cy, cx = self.pad[self.pos]
        ny, nx = self.pad[target]
        self.pos = target

        return nx - cx, ny - cy


class KeyPad(Pad):
    def __init__(self):
        super().__init__()
        self.pad = {
            "A": (0,0),
            "^": (0,1),
            ">": (1,0),
            "v": (1,1),
            "<": (1,2),
        }
        self.type = "KeyPad"


def solve_part1(the_data: list[str]):
    """Solve the puzzle."""
    solution1 = 0

    r2 = NumPad()

    # length of the shortest sequence * numeric part of the code
    for code in the_data:
        sum_dx = 0
        sum_dy = 0
        for num in code:
            if num == "A":
                dx, dy = np.activate()
            else:
                dx, dy = np.move_to(num)
            sum_dx += dx
            sum_dy += dy

    return solution1


def solve_part2(the_data: list[str]):
    """Solve the puzzle."""
    solution2 = 0

    return solution2


if __name__ == "__main__":
    # the_data = get_data("2024/data/day21.data")
    the_data = get_data("2024/data/day21.test")
    time_start = time.perf_counter()
    solution1 = solve_part1(the_data)
    print(f"Part 1 ({solution1}) solved in {time.perf_counter()-time_start:.5f} Sec.")
    time_start = time.perf_counter()
    solution2 = solve_part2(the_data)
    print(f"Part 2 ({solution2}) solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

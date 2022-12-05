#!/usr/bin/env python3
""" Advent of Code 2022/12/05
https://adventofcode.com/2022/day/5
"""


def main():
    """
    the main function of the module
    """
    with open("data.txt", "r") as in_file:
        the_plan = [line for line in in_file]

    stacks = {}
    split_idx = the_plan.index("\n")

    for col, val in enumerate(the_plan[split_idx - 1]):
        if val != " ":
            stacks[val] = []
            for items in the_plan[: split_idx - 1]:
                if items[col] != " ":
                    stacks[val].insert(0, items[col])

    for move in the_plan[split_idx + 1 :]:
        move = move.split()
        cnt = int(move[1])
        src = move[3]
        dst = move[5]
        for _ in range(cnt):
            item = stacks[src].pop()
            stacks[dst].append(item)

    for stack in stacks.keys():
        print(stacks[stack][-1], end="")
    print()

#    # devide the plan
#    for line in the_plan:
#        if line == "":
#            in_stack_plan = False
#
#        if in_stack_plan:
#            stack_plan.append(line)
#        else:
#            moves.append(line.split())
#
#
#    print(f"Total: {total}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
""" Advent of Code 2022/12/19
https://adventofcode.com/2022/day/19

Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.
"""

from collections import deque


def get_data(filename: str) -> list:
    """
    Return file contents as list
    """
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def nq_sort(status):
    """https://www.youtube.com/watch?v=3-VJC_KRUZ0&t=330s"""
    _, _, _, _, _, _, _, _, w, x, y, z = status
    return 1 * w + 10 * x + 100 * y + 1000 * z


def main():
    """code if module is called directly"""
    # the_data = get_data("data_test1.txt")
    the_data = get_data("data.txt")

    candidates = {}
    best = []

    for data in the_data[:3]:
        blueprint = data.split(":")[0]
        blueprint = blueprint.split()
        lines = data.split("costs")
        # costs = (ore, clay, (obsidian), (geodes))
        bot_cost = (
            int(lines[1].split()[0]),
            int(lines[2].split()[0]),
            (int(lines[3].split()[0]), int(lines[3].split()[3])),
            (int(lines[4].split()[0]), int(lines[4].split()[3])),
        )

        # bots = (ore, clay, obsidian, geodes)
        _bots = (1, 0, 0, 0)

        print(f"*** {blueprint} ***")
        # print(f"{bot_cost=}")

        minutes = 0
        next_nodes = set([_bots + (0, 0, 0, 0) + (0, 0, 0, 0)])

        while minutes < 32:  # 24
            minutes += 1
            # print(f"Start of Minute {minutes}")
            nodes = deque(sorted(next_nodes, key=nq_sort, reverse=True)[:1000])
            # print(f"{minutes=}: {len(nodes)=}")
            next_nodes.clear()
            while nodes:
                (
                    b_ore,
                    b_clay,
                    b_obs,
                    b_geo,
                    m_ore,
                    m_clay,
                    m_obs,
                    m_geo,
                    a_ore,
                    a_clay,
                    a_obs,
                    a_geo,
                ) = nodes.popleft()

                # ore to work with
                c_ore = m_ore
                c_clay = m_clay
                c_obs = m_obs
                c_geo = m_geo

                # produce ore, +1 per bot
                n_ore = m_ore + b_ore
                n_clay = m_clay + b_clay
                n_obs = m_obs + b_obs
                n_geo = m_geo + b_geo

                a_ore += b_ore
                a_clay += b_clay
                a_obs += b_obs
                a_geo += b_geo

                # spend material in production, we can build one bot per round,
                # but which one? This is a one of multi choice
                if c_ore >= bot_cost[0]:
                    next_nodes.add(
                        (
                            b_ore + 1,
                            b_clay,
                            b_obs,
                            b_geo,
                            n_ore - bot_cost[0],
                            n_clay,
                            n_obs,
                            n_geo,
                            a_ore,
                            a_clay,
                            a_obs,
                            a_geo,
                        ),
                    )
                if c_ore >= bot_cost[1]:
                    next_nodes.add(
                        (
                            b_ore,
                            b_clay + 1,
                            b_obs,
                            b_geo,
                            n_ore - bot_cost[1],
                            n_clay,
                            n_obs,
                            n_geo,
                            a_ore,
                            a_clay,
                            a_obs,
                            a_geo,
                        ),
                    )
                if c_ore >= bot_cost[2][0] and c_clay >= bot_cost[2][1]:
                    next_nodes.add(
                        (
                            b_ore,
                            b_clay,
                            b_obs + 1,
                            b_geo,
                            n_ore - bot_cost[2][0],
                            n_clay - bot_cost[2][1],
                            n_obs,
                            n_geo,
                            a_ore,
                            a_clay,
                            a_obs,
                            a_geo,
                        ),
                    )
                if c_ore >= bot_cost[3][0] and c_obs >= bot_cost[3][1]:
                    next_nodes.add(
                        (
                            b_ore,
                            b_clay,
                            b_obs,
                            b_geo + 1,
                            n_ore - bot_cost[3][0],
                            n_clay,
                            n_obs - bot_cost[3][1],
                            n_geo,
                            a_ore,
                            a_clay,
                            a_obs,
                            a_geo,
                        ),
                    )
                # the conservative bot does nothing
                next_nodes.add(
                    (
                        b_ore,
                        b_clay,
                        b_obs,
                        b_geo,
                        n_ore,
                        n_clay,
                        n_obs,
                        n_geo,
                        a_ore,
                        a_clay,
                        a_obs,
                        a_geo,
                    ),
                )
            # print(f"End of Minute {minutes}")
        else:
            geodes = set()
            for (
                b_ore,
                b_clay,
                b_obs,
                b_geo,
                m_ore,
                m_clay,
                m_obs,
                m_geo,
                a_ore,
                a_clay,
                a_obs,
                a_geo,
            ) in next_nodes:
                geodes.add(m_geo)

        candidates[f'{" ".join(blueprint)}'] = {
            "max": max(geodes),
            "quality": int(blueprint[1]) * max(geodes),
        }
        best.append(max(geodes))

    print(candidates)
    solution = 1
    for b in best:
        solution *= b
    return solution


if __name__ == "__main__":
    solution = main()
    print(f"{solution=}")

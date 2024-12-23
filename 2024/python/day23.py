"""Solve Advent of Code 2024, day 23

https://adventofcode.com/2024/day/23
"""

import time
from collections import defaultdict
from collections import deque
from itertools import combinations


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    return content


def parse_data(the_data: list[str]) -> dict[str, set[str]]:
    """
    Parse the input data and construct a graph as an adjacency list.

    Args:
        the_data (list[str]): The input data.

    Returns:
        dict[str, set[str]]: Adjacency list representing the graph.
    """
    graph = defaultdict(set)
    for line in the_data:
        node1, node2 = line.split("-")
        graph[node1].add(node2)
        graph[node2].add(node1)

    return graph


def solve_part1(graph: dict[str, set[str]]) -> int:
    """
    Find all groups of computers of size 3 in the graph.

    Args:
        graph (dict[str, set[str]]): The adjacency list representation of the graph.

    Returns:
        list[tuple[str, str, str]]: List of all groups of size 3.
    """
    solution = 0
    groups = []
    for node in graph:
        neighbors = graph[node]
        for node1, node2 in combinations(neighbors, 2):
            if node1 in graph[node2]:
                group = tuple(sorted([node, node1, node2]))
                groups.append(group)

    for group in sorted(set(groups)):
        if any(node.startswith("t") for node in group):
            # print(f"group: {group} has at least one t-node")
            solution += 1

    # groups = sorted(set(groups))
    # return sum(1 for group in groups if any(node.startswith("t") for node in group))

    return solution


def solve_part2(graph: dict[str, set[str]]) -> str:
    """
    Find the largest group in the graph using a tree-based approach.

    Args:
        graph (dict[str, set[str]]): The adjacency list representation of the graph.

    Returns:
        str: Comma-separated names of the computers in the largest group.
    """

    def expand_group(node: str, current_group: set[str]) -> set[str]:
        """
        Expand the group starting from the given node.

        Args:
            node (str): The starting node.
            current_group (set[str]): The current set of nodes in the group.

        Returns:
            set[str]: The largest group starting from the given node.
        """
        neighbors = graph[node]
        for neighbor in neighbors:
            # Check if the neighbor is connected to all nodes in the current group
            if all(neighbor in graph[other] for other in current_group):
                # Add the neighbor to the group and continue expanding
                current_group.add(neighbor)
                expand_group(neighbor, current_group)
        return current_group

    largest_group = set()
    for node in graph:
        group = expand_group(node, {node})
        if len(group) > len(largest_group):
            largest_group = group

    # co,de,ka,ta
    # Return the group as a sorted, comma-separated string
    return ",".join(sorted(largest_group))


if __name__ == "__main__":
    solution1 = solution2 = 0
    the_data = get_data("2024/data/day23.data")
    # the_data = get_data("2024/data/day23.test")
    
    graph = parse_data(the_data=the_data)

    time_start = time.perf_counter()
    solution1 = solve_part1(graph)
    print(f"Part 1 ({solution1}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    time_start = time.perf_counter()
    solution2 = solve_part2(graph)
    print(f"Part 2 ({solution2}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # finally
    print(f"{solution1=} | {solution2=}")

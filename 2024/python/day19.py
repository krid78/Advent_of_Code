"""""Solve Advent of Code 2024, day 19

https://adventofcode.com/2024/day/19
"""

import heapq
import time


def get_data(filename: str) -> tuple[list[tuple], list[str]]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    available_patterns = [(len(p.strip()), p.strip()) for p in content[0].split(",")]
    designs = content[2:]

    return available_patterns, designs


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_pattern = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_pattern = True

    def find_prefixes(self, design, start_index):
        """
        Find all prefixes in the trie that match the design starting at start_index.
        """
        node = self.root
        prefixes = []
        for i in range(start_index, len(design)):
            char = design[i]
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end_of_pattern:
                prefixes.append(i + 1)  # End index of the prefix
        return prefixes

    def to_dot(self, filename="trie.dot"):
        """
        Generate a Graphviz DOT file to visualize the trie.

        Args:
            filename (str): The output DOT file name.
        """
        dot_lines = ["digraph Trie {", "    node [shape=circle];"]

        def traverse(node, parent_id):
            nonlocal node_id
            current_id = node_id
            node_id += 1

            if parent_id is not None:
                dot_lines.append(f"    {parent_id} -> {current_id};")

            if node.is_end_of_pattern:
                dot_lines.append(f"    {current_id} [shape=doublecircle];")

            for char, child in node.children.items():
                child_id = traverse(child, current_id)
                dot_lines.append(f"    {current_id} -> {child_id} [label=\"{char}\"];")

            return current_id

        node_id = 0
        traverse(self.root, None)

        dot_lines.append("}")

        with open(filename, "w") as f:
            f.write("\n".join(dot_lines))


def build_trie(patterns):
    """
    Build a Trie from the given patterns.
    """
    trie = Trie()
    for _, pattern in patterns:
        trie.insert(pattern)
    return trie


def can_form_design(trie, design):
    """
    Check if the design can be formed using the available patterns with dynamic programming.
    """
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always formable

    for i in range(n):
        if not dp[i]:
            continue
        # Find all prefixes starting at index i
        for end_index in trie.find_prefixes(design, i):
            dp[end_index] = True

    return dp[n]


def count_representations(trie, design):
    """
    Count the number of ways a design can be formed using available patterns.

    Args:
        trie (Trie): The Trie built from available patterns.
        design (str): The design string to check.

    Returns:
        int: The number of representations for the design.
    """
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1  # One way to form an empty string

    for i in range(n):
        if dp[i] == 0:
            continue
        # Find all prefixes starting at index i
        for end_index in trie.find_prefixes(design, i):
            dp[end_index] += dp[i]

    return dp[n]


def solve_part1(patterns, designs):
    """
    Solve part 1: Check which designs can be formed using the patterns.

    Args:
        patterns (list[tuple[int, str]]): List of available patterns with their lengths.
        designs (list[str]): List of designs to check.

    Returns:
        dict: Mapping of designs to whether they can be formed.
    """
    trie = build_trie(patterns)
    results = {}

    for design in designs:
        results[design] = count_representations(trie, design)

    trie.to_dot("trie_visualization.dot")  # Generate visualization for debugging

    return results


def solve(test=False):
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    if test:
        available_patterns, designs = get_data("2024/data/day19.test")
    else:
        available_patterns, designs = get_data("2024/data/day19.data")

    length_designs = len(designs)
    longest_design = max(len(l) for l in designs)
    length_av_patterns = len(available_patterns)
    longest_pattern = max(l for l, _ in available_patterns)

    print(
        "=" * 10
        + f"Statistics: {length_designs=}, {longest_design=}, {length_av_patterns=}, {longest_pattern=}"
        + "=" * 10
    )

    time_start = time.perf_counter()
    design_matches = solve_part1(available_patterns, designs)
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    # print(design_matches)

    for _, count in design_matches.items():
        solution1 += count

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve(test=True)
    # solution1, solution2 = solve(test=False)
    print(f"{solution1=} | {solution2=}")

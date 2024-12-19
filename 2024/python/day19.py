"""Solve Advent of Code 2024, day 19

https://adventofcode.com/2024/day/19
"""

import heapq
import time
import logging
from typing import List, Tuple, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_data(filename: str) -> Tuple[List[Tuple[int, str]], List[str]]:
    """
    Parse file contents into available patterns and designs.

    Args:
        filename (str): Path to the input file.

    Returns:
        Tuple[List[Tuple[int, str]], List[str]]: Available patterns with lengths and design strings.
    """
    with open(filename, "r") as in_file:
        content = [row.rstrip() for row in in_file]

    available_patterns = [(len(p.strip()), p.strip()) for p in content[0].split(",")]
    designs = content[2:]

    return available_patterns, designs


class TrieNode:
    def __init__(self) -> None:
        """Initialize a Trie node."""
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end_of_pattern: bool = False


class Trie:
    def __init__(self) -> None:
        """Initialize a Trie."""
        self.root = TrieNode()

    def insert(self, pattern: str) -> None:
        """
        Insert a pattern into the trie.

        Args:
            pattern (str): The pattern to insert.
        """
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_pattern = True

    def find_prefixes(self, design: str, start_index: int) -> List[int]:
        """
        Find all prefixes in the trie that match the design starting at start_index.

        Args:
            design (str): The design string.
            start_index (int): The index to start searching from.

        Returns:
            List[int]: End indices of all matching prefixes.
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

    def to_dot(self, filename: str = "trie.dot") -> None:
        """
        Generate a Graphviz DOT file to visualize the trie.

        Args:
            filename (str): The output DOT file name.
        """
        dot_lines = ["digraph Trie {", "    node [shape=circle];"]

        def traverse(node: TrieNode, parent_id: int) -> int:
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


def build_trie(patterns: List[Tuple[int, str]]) -> Trie:
    """
    Build a Trie from the given patterns.

    Args:
        patterns (List[Tuple[int, str]]): List of patterns with their lengths.

    Returns:
        Trie: A Trie containing the patterns.
    """
    trie = Trie()
    for _, pattern in patterns:
        trie.insert(pattern)
    return trie


def can_form_design(trie: Trie, design: str) -> bool:
    """
    Check if the design can be formed using the available patterns with dynamic programming.

    Args:
        trie (Trie): The Trie built from available patterns.
        design (str): The design string to check.

    Returns:
        bool: True if the design can be formed, False otherwise.
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


def count_representations(trie: Trie, design: str) -> int:
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
            logger.debug(
                f"dp[{end_index}] updated to {dp[end_index]} using prefix ending at index {end_index}"
            )

    logger.info(f"Total representations for '{design}': {dp[n]}")
    return dp[n]


def solve_part1(patterns: List[Tuple[int, str]], designs: List[str]) -> Dict[str, int]:
    """
    Solve part 1: Check how many representations each design has using the patterns.

    Args:
        patterns (List[Tuple[int, str]]): List of available patterns with their lengths.
        designs (List[str]): List of designs to check.

    Returns:
        Dict[str, int]: Mapping of designs to the number of representations.
    """
    trie = build_trie(patterns)
    results = {}

    for design in designs:
        results[design] = count_representations(trie, design)

    trie.to_dot("trie_visualization.dot")  # Generate visualization for debugging

    return results


def solve(test: bool = False) -> Tuple[int, int]:
    """
    Solve the puzzle.

    Args:
        test (bool): Whether to run with test data.

    Returns:
        Tuple[int, int]: Solution for part 1 and part 2.
    """
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
        + f" Statistics: {length_designs=}, {longest_design=}, {length_av_patterns=}, {longest_pattern=} "
        + "=" * 10
    )

    time_start = time.perf_counter()
    design_matches = solve_part1(available_patterns, designs)
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")

    for _, count in design_matches.items():
        solution1 += count

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve(test=True)
    # solution1, solution2 = solve(test=False)
    print(f"{solution1=} | {solution2=}")

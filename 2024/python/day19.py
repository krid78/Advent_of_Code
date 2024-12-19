"""Solve Advent of Code 2024, day 19

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


def solve_part1(av_patterns: list[tuple], designs: list[str]):
    """
    Find all designs that can be represented by available patterns.

    Args:
        av_patterns (list[tuple]): List of (length, pattern) tuples.
        designs (list[str]): List of design strings.

    Returns:
        dict: A dictionary where keys are designs and values are lists of match counts.
    """
    # Sort patterns by length (longest first)
    av_patterns.sort(reverse=True)

    # Initialize data structures
    candidates = []
    design_matches = {}

    # Populate the initial heap
    for idx, design in enumerate(designs):
        for length, pattern in av_patterns:
            if design.startswith(pattern):
                remaining = design.removeprefix(pattern)
                heapq.heappush(candidates, (idx, remaining, len(remaining), 1))

    # Process candidates
    while candidates:
        idx, remaining, remaining_length, match_count = heapq.heappop(candidates)

        # If the string is fully matched
        if remaining_length == 0:
            design_matches.setdefault(designs[idx], []).append(match_count)
            continue

        # Try to match remaining string with available patterns
        for length, pattern in av_patterns:
            if remaining.startswith(pattern):
                new_remaining = remaining.removeprefix(pattern)
                heapq.heappush(
                    candidates,
                    (idx, new_remaining, remaining_length - length, match_count + 1),
                )

    return design_matches


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_pattern = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pattern: str):
        """
        Insert a pattern into the trie.
        """
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_pattern = True

    def find_prefixes(self, string: str) -> list[str]:
        """
        Find all prefixes of `string` that exist in the trie.

        Args:
            string (str): The input string to match prefixes.

        Returns:
            list[str]: A list of prefixes found in the trie.
        """
        prefixes = []
        node = self.root
        current_prefix = ""

        for char in string:
            if char not in node.children:
                break
            current_prefix += char
            node = node.children[char]
            if node.is_end_of_pattern:
                prefixes.append(current_prefix)

        return prefixes


def solve_part1_with_trie(
    patterns: list[str], designs: list[str]
) -> dict[str, list[int]]:
    """
    Solve the problem using a Trie for pattern matching.

    Args:
        patterns (list[str]): List of available substrings.
        designs (list[str]): List of design strings.

    Returns:
        dict[str, list[int]]: A dictionary where keys are designs and values are lists of match counts.
    """
    # Initialize Trie
    trie = Trie()
    for _, pattern in patterns:
        trie.insert(pattern)

    design_matches = {}

    # Process each design
    for design in designs:
        queue = [(design, 0)]  # (remaining string, match count)
        matches = []

        while queue:
            current_string, match_count = queue.pop(0)

            if not current_string:
                matches.append(match_count)
                continue

            prefixes = trie.find_prefixes(current_string)
            for prefix in prefixes:
                queue.append((current_string[len(prefix) :], match_count + 1))

        if matches:
            design_matches[design] = matches

    return design_matches


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
    longest_pattern = max(l for l,_ in available_patterns)

    print("=" * 10 + f"Statistics: {length_designs=}, {longest_design=}, {length_av_patterns=}, {longest_pattern=}" + "=" * 10)

    # design_matches = solve_part1(available_patterns, designs)
    # design_matches = solve_part1_with_trie(available_patterns, designs)
    # print(design_matches)
    # solution1 = len(design_matches)

    return solution1, solution2


if __name__ == "__main__":
    time_start = time.perf_counter()
    solution1, solution2 = solve(test=False)
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
    print(f"{solution1=} | {solution2=}")

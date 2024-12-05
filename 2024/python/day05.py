"""Solve Advent of Code 2024, day 5

https://adventofcode.com/2024/day/5
"""


def get_data(filename: str) -> list[str]:
    """Return file contents as a list of strings."""
    with open(filename, "r") as in_file:
        return [row.rstrip() for row in in_file]


def build_page_map(data: list[str]) -> dict[int, list[int]]:
    """
    Build the page map from the input data.

    Args:
        data: List of strings in the format 'pre|post'.

    Returns:
        Dictionary mapping 'pre' to a list of 'post' values.
    """
    page_map = {}
    for line in data:
        pre, post = map(int, line.split("|"))
        page_map.setdefault(pre, []).append(post)
    return page_map


def process_update_list(
    update_list: list[int], page_map: dict[int, list[int]]
) -> tuple[bool, int]:
    """
    Process an update list to resolve conflicts based on the page map.

    Args:
        update_list: The list of numbers to process.
        page_map: The dictionary of page mappings.

    Returns:
        A tuple containing:
        - A boolean indicating if the list is correct.
        - The middle value of the processed list.
    """
    correct = True
    idx = 0

    while idx < len(update_list):
        current = update_list[idx]
        left = set(update_list[:idx])
        right = set(page_map.get(current, []))

        if left & right:
            # Conflict detected
            correct = False
            intersection = left & right
            earliest_position = min(update_list.index(x) for x in intersection)
            update_list.pop(idx)
            update_list.insert(earliest_position, current)
            idx = earliest_position
        else:
            idx += 1

    middle_value = update_list[len(update_list) // 2]
    return correct, middle_value


def solve() -> tuple[int, int]:
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    # Load data
    the_data = get_data("2024/data/day05.data")
    # the_data = get_data("2024/data/day05.test")

    # Split data into page map and updates
    upd_start = the_data.index("")
    page_map = build_page_map(the_data[:upd_start])
    update_lists = [
        list(map(int, line.split(","))) for line in the_data[upd_start + 1 :]
    ]

    # Process each update list
    for update_list in update_lists:
        correct, middle_value = process_update_list(update_list, page_map)
        if correct:
            solution1 += middle_value
        else:
            solution2 += middle_value

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
    print(f"{solution1=} | {solution2=}")

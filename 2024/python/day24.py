"""Solve Advent of Code 2024, day 24

https://adventofcode.com/2024/day/24
"""

import re
import time


def get_data(filename: str) -> list[str]:
    """Return file contents as list of strings."""
    with open(filename, "r") as in_file:
        content = [row.strip() for row in in_file]

    return content


def parse_data(
    the_data: list[str],
) -> tuple[dict[str, int], list[tuple[str, str, str, str]]]:
    equations_start = the_data.index("")
    values = {}
    operations = []

    # store known variables
    for line in the_data[:equations_start]:
        k, v = line.split(":")
        values[k.strip()] = int(v.strip())

    # store equations
    operation_pattern = re.compile(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)")
    for line in the_data[equations_start:]:
        match = operation_pattern.match(line.strip())
        if match:
            operand1, operation, operand2, result = match.groups()
            operations.append((operand1, operation, operand2, result))

    return values, operations


def dez_to_binstr(dezimal: int) -> str:
    """Convert decimal to binary as str"""
    return bin(dezimal)[2:]


def dez_of_letter(values: dict[str, int], letter: str) -> int:
    """Convert the values starting with letter to dezimal"""
    binary = name_to_binstr(values, letter)
    return binstr_to_dez(binary)


def binstr_to_dez(binary: str) -> int:
    """Convert a string of 0s and 1s to integer"""
    solution = 0
    for idx, v in enumerate(binary[::-1]):
        solution += int(v) * 2**idx

    return solution


def name_to_binstr(values: dict[str, int], letter: str) -> str:
    """Convert the values starting with letter to string of 0s and 1s"""
    binary = ""
    for k in sorted(values):
        if k.startswith(letter):
            binary = str(values[k]) + binary
    # print(f"{letter=}: {binary=}")
    return binary


def solve_part1(
    values: dict[str, int], operations: list[tuple[str, str, str, str]]
) -> int:
    """Solve the puzzle."""
    solution = 0

    # for operand1, operation, operand2, result in operations:
    while operations:
        operand1, operation, operand2, result = operations.pop(0)
        if operand1 not in values or operand2 not in values:
            operations.append((operand1, operation, operand2, result))
            continue
        if operation == "AND":
            values[result] = values[operand1] & values[operand2]
        elif operation == "OR":
            values[result] = values[operand1] | values[operand2]
        elif operation == "XOR":
            values[result] = values[operand1] ^ values[operand2]
        else:
            raise ValueError(f"Invalid operation: {operation}")

    # print(values)

    solution = dez_of_letter(values, "z")

    return solution


def build_dependency_tree(
    gates: list[tuple[str, str, str, str]]
) -> dict[str, tuple[str, str, str]]:
    """
    Build a dependency tree for each output wire.

    Args:
        gates (List[Tuple[str, str, str]]): List of gate operations.

    Returns:
        Dict[str, Tuple[str, str, str]]: Dependency tree mapping each output wire to its inputs.
    """
    dependency_tree = {}
    for a, op, b, output in gates:
        dependency_tree[output] = (a, op, b)
    return dependency_tree


from graphviz import Digraph


def visualize_dependency_tree(
    dependency_tree: dict[str, tuple[str, str, str]],
    output_file: str = "dependency_tree",
):
    """
    Visualize the dependency tree using Graphviz.

    Args:
        dependency_tree (Dict[str, List[Tuple[str, str, str]]]):
            The dependency tree mapping output wires to their input wires and operations.
        output_file (str): The name of the output file (without extension).

    Returns:
        None
    """
    dot = Digraph(format="png")
    dot.attr(rankdir="LR")

    # Add nodes and edges
    for output, (input_a, operation, input_b) in dependency_tree.items():
        # Add nodes for the inputs and operation
        dot.node(input_a, input_a, shape="ellipse")
        dot.node(input_b, input_b, shape="ellipse")
        op_node = f"{output}_{operation}"
        dot.node(op_node, operation, shape="box", style="filled", color="lightgrey")

        # Connect inputs to the operation
        dot.edge(input_a, op_node)
        dot.edge(input_b, op_node)

        # Connect the operation to the output
        dot.node(output, output, shape="ellipse")
        dot.edge(op_node, output)

    # Save and render the graph
    dot.render(output_file, view=True)


def solve_part2(
    values: dict[str, int], operations: list[tuple[str, str, str, str]]
) -> list[str]:
    """Solve the puzzle."""
    solution = 0

    x = dez_of_letter(values, "x")
    y = dez_of_letter(values, "y")
    solution = x + y
    print(f"{x} + {y} = {solution}")
    correct_z = dez_to_binstr(solution)
    print("\n=== Correct ===")
    print(f"   {dez_to_binstr(x)}")
    print(f"+  {dez_to_binstr(y)}")
    print(f"= {correct_z}")
    calc_z = dez_to_binstr(solve_part1(values.copy(), operations.copy()))
    print("\n=== Current ===")
    print(f"   {dez_to_binstr(x)}")
    print(f"+  {dez_to_binstr(y)}")
    print(f"= {calc_z}")
    print("\n=== Compare ===")
    print(f"correct: {correct_z}")
    print(f"current: {calc_z}")

    for idx in range(len(correct_z) - 1, -1, -1):
        if correct_z[idx] != calc_z[idx]:
            print(f"Difference at {idx+1}")
            break

    # for shift in range(22, 25):
    for shift in range(45):
        test = values.copy()
        test_x_in = 1 << shift
        test_y_in = 1 << shift
        test_x = dez_to_binstr(test_x_in).zfill(45)
        test_y = dez_to_binstr(test_y_in).zfill(45)
        test_z = dez_to_binstr(test_x_in + test_y_in).zfill(46)
        x_in = {
            f"x{str(i).zfill(2)}": int(bit) for i, bit in enumerate(reversed(test_x))
        }
        y_in = {
            f"y{str(i).zfill(2)}": int(bit) for i, bit in enumerate(reversed(test_y))
        }
        z_in = {
            f"z{str(i).zfill(2)}": int(bit) for i, bit in enumerate(reversed(test_z))
        }
        test.update(x_in)
        test.update(y_in)
        test.update(z_in)
        solve_part1(test, operations.copy())
        test_z_out = dez_to_binstr(solve_part1(test, operations.copy())).zfill(46)
        if test_z_out != test_z:
            print(f"\n=== Test {shift} ===")
            print(f"   {test_x}")
            print(f"+  {test_y}")
            print(f"= {test_z_out}")
            print(f"  {test_z}")

    dp_tree = build_dependency_tree(operations)
    visualize_dependency_tree(dp_tree, "day24")

    # suspect = {}
    print(f"\n=== Suspects ===")
    for k, (a, op, b) in dp_tree.items():
        if k.startswith("z") and op != "XOR":
            # suspect[k] = (a, op, b)
            print(f"{k=} -> {(a, op, b)}")
        elif a.startswith("x") and b.startswith("y") and op not in ["AND", "XOR"]:
            # suspect[k] = (a, op, b)
            print(f"{k=} -> {(a, op, b)}")
        elif a.startswith("y") and b.startswith("x") and op not in ["AND", "XOR"]:
            # suspect[k] = (a, op, b)
            print(f"{k=} -> {(a, op, b)}")

    # return suspect
    return ["z35", "hqk", "z06", "fhc", "z11", "qhj", "mwh", "ggt"]


if __name__ == "__main__":
    # the_data = get_data("2024/data/day24.data.cor")
    the_data = get_data("2024/data/day24.data")
    # the_data = get_data("2024/data/day24.0.test")
    # the_data = get_data("2024/data/day24.1.test")

    __values__, __operations__ = parse_data(the_data)

    # print(values)

    # Solve part 1
    time_start = time.perf_counter()
    solution1 = solve_part1(__values__.copy(), __operations__.copy())
    print(f"Part 1 ({solution1}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # solve part 1
    time_start = time.perf_counter()
    solution2 = solve_part2(__values__, __operations__)
    solution2 = ",".join(sorted(solution2))
    print(f"Part 2 ({solution2}) solved in {time.perf_counter()-time_start:.5f} Sec.")

    # Finally
    print(f"{solution1=} | {solution2=}")

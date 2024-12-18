"""Solve Advent of Code 2024, day 17

https://adventofcode.com/2024/day/17
"""

import time


def get_data(test: bool) -> tuple[list[int], list[int]]:
    """Return the register values and the code

    Args:
        test (bool): Test data or production code

    Returns:
        tuple[list[int], list[int]]: Register values A, B, C and Programm Code
    """
    if test:
        registers = [729, 0, 0]
        program = [0, 1, 5, 4, 3, 0]
    else:
        registers = [64854237, 0, 0]
        program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 0, 5, 5, 0, 3, 3, 0]

    return registers, program


def run_program(registers, program):
    """
    Simulate the execution of the 3-bit computer program.

    Args:
        registers: A tuple/list [A, B, C] representing initial register values.
        program: A list of integers representing the program instructions.

    Returns:
        A string representing the program's output (comma-separated values).
    """
    # Initialize registers A, B, C
    A, B, C = registers
    # Instruction pointer starts at 0
    ip = 0
    output = []  # List to store outputs

    # Combo operand value resolution
    def resolve_combo_operand(operand):
        if operand <= 3:  # Literal values 0-3
            # print(f"return {operand=}")
            return operand
        elif operand == 4:  # Value of register A
            # print("return A")
            return A
        elif operand == 5:  # Value of register B
            # print("return B")
            return B
        elif operand == 6:  # Value of register C
            # print("return C")
            return C
        elif operand == 7:  # Reserved
            raise ValueError("Invalid combo operand: 7")

    # Program execution loop
    while ip < len(program):
        opcode = program[ip]  # Current instruction opcode
        operand = program[ip + 1]  # Operand
        # print(f"{opcode=}, {operand=}, {A=}")
        if opcode == 0:  # adv: A = A // 2^(combo_operand)
            # print("A = A // 2^(combo_operand)")
            A //= 2 ** resolve_combo_operand(operand)
        elif opcode == 1:  # bxl: B = B ^ literal_operand
            # print("B = B ^ literal_operand")
            B ^= operand
        elif opcode == 2:  # bst: B = combo_operand % 8
            # print("B = combo_operand % 8")
            B = resolve_combo_operand(operand) % 8
        elif opcode == 3:  # jnz: if A != 0, jump to literal_operand
            if A != 0:
                # print("if A != 0, jump to literal_operand\n")
                ip = operand
                continue
            # print(f"No Jump, {A=}\n")
        elif opcode == 4:  # bxc: B = B ^ C (operand ignored)
            # print("B = B ^ C (operand ignored)")
            B ^= C
        elif opcode == 5:  # out: output combo_operand % 8
            # print("output combo_operand % 8")
            output.append(resolve_combo_operand(operand) % 8)
            # print(f"New {output=}")
        elif opcode == 6:  # bdv: B = A // 2^(combo_operand)
            # print("B = A // 2^(combo_operand)")
            B = A // 2 ** resolve_combo_operand(operand)
        elif opcode == 7:  # cdv: C = A // 2^(combo_operand)
            # print("C = A // 2^(combo_operand)")
            C = A // 2 ** resolve_combo_operand(operand)
        else:
            raise ValueError(f"Invalid opcode: {opcode}")

        # Move to the next instruction (increment by 2)
        ip += 2

    # Join the output values with commas
    return ",".join(map(str, output))


def find_a(registers, program, prg_pos):
    a, b, c = registers
    if abs(prg_pos) > len(program):
        return a
    for i in range(8):
        first_digit_out = run_program([a * 8 + i, b, c], program)
        if int(first_digit_out[0]) == program[prg_pos]:
            e = find_a([a * 8 + i, b, c], program, prg_pos - 1)
            if e:
                return e


def solve():
    """Solve the puzzle."""
    solution1 = 0
    solution2 = 0

    test = False
    # registers, program = get_data(test=False)
    registers, program = get_data(test=test)

    if test:
        print(f"{run_program([0, 0, 9], [2,6])=}")  # set register B to 1.
        print(f"{run_program([10, 0, 0], [5,0,5,1,5,4])=}")  # output 0,1,2.
        print(
            f"{run_program([2024,0,0], [0,1,5,4,3,0])=}"
        )  # 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
        print(f"{run_program([0, 29, 0], [1,7])=}")  # B to 26.
        print(f"{run_program([0, 2024 , 43690], [4,0])=}")  # B to 44354.

    time_start = time.perf_counter()
    solution1 = run_program(registers, program)
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")

    time_start = time.perf_counter()
    solution2 = find_a([0, 0, 0], program, -1)
    print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = solve()
    print(f"{solution1=} | {solution2=}")

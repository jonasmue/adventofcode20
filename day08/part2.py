from common import *


def flip_operation(instructions, i):
    op, _ = instructions[i]
    if op == "nop": instructions[i][0] = "jmp"
    elif op == "jmp": instructions[i][0] = "nop"


def find_correct_program():
    # O(n^2) time and O(n) space
    instructions = get_input()
    for i in range(len(instructions)):
        flip_operation(instructions, i)
        computer = Computer(instructions)
        computer.run()
        if computer.finished: return computer.accumulator
        flip_operation(instructions, i)


if __name__ == "__main__":
    print(find_correct_program())

def get_input():
    with open("input.txt") as f:
        instructions = []
        for line in f.read().splitlines():
            operation = line.split("=")
            if operation[0].startswith("mask"):
                instructions.append((operation[0].strip(), operation[1].strip()))
            else:
                address = operation[0].split("]")[0][4:]
                instructions.append((int(address), int(operation[1].strip())))
        return instructions


def set_nth_bit(x, n):
    return x | (1 << n)


def unset_nth_bit(x, n):
    return x & ~(1 << n)
    
             
class Computer():
    
    def __init__(self):
        self.memory = {}
        self.instructions = get_input()

    def run_program(self, process):
        for operation, argument in self.instructions:
            self.current_operation = operation
            if operation == "mask":
                self.current_mask = argument
                continue
            self.current_argument = argument
            process(self)

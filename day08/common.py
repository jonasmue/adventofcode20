class Computer():
    def __init__(self, instructions):
        self.instructions = instructions
        self.pointer = 0
        self.accumulator = 0
        self.history = set()
        self.finished = False
    
    def exec_instruction(self):
        op, arg = self.instructions[self.pointer]
        if op == "nop":
            self.pointer += 1
        elif op == "acc":
            self.pointer += 1
            self.accumulator += int(arg)
        elif op == "jmp":
            self.pointer += int(arg)
    
    def run(self):
        while self.pointer not in self.history:
            if self.pointer >= len(self.instructions):
                self.finished = True
                return
            self.history.add(self.pointer)
            self.exec_instruction()    
    

def get_input():
    with open("input.txt") as f:
        instruction_lines = f.read().splitlines()
        instructions = [l.split() for l in instruction_lines]
        return instructions

from common import *


def process(computer):
    computer.memory[computer.current_operation] = apply_mask(computer.current_mask, computer.current_argument)
    

def apply_mask(mask, number, overwrite_zero=True):
    for bit_index in range(len(mask)):
        current_mask_token = mask[bit_index]
        if current_mask_token == "X": continue
        offset = len(mask) - bit_index - 1
        if current_mask_token == "1":
            number = set_nth_bit(number, offset)
        else:
            number = unset_nth_bit(number, offset)
    return number


if __name__ == "__main__":
    computer = Computer()
    computer.run_program(process)
    print(sum(computer.memory.values()))

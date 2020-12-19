from common import *


def process(computer):
    for address in get_addresses(computer.current_mask, computer.current_operation):
        computer.memory[address] = computer.current_argument
        

def get_addresses(mask, address):
    result = [address]
    for bit_index in range(len(mask)):
        offset = len(mask) - bit_index - 1
        current_mask_token = mask[bit_index]
        if current_mask_token == "X":
            result += result
            for i in range(len(result)//2):
                result[i] = unset_nth_bit(result[i], offset)
            for i in range(len(result)//2, len(result)):
                result[i] = set_nth_bit(result[i], offset)
        elif current_mask_token == "1":
            for i in range(len(result)):
                result[i] = set_nth_bit(result[i], offset)
    return result
    

if __name__ == "__main__":
    computer = Computer()
    computer.run_program(process)
    print(sum(computer.memory.values()))

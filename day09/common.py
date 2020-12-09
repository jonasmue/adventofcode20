from collections import deque


def get_input():
    with open("input.txt") as f:
        return [int(line) for line in f.read().splitlines()]
        
        
def check_valid(preamble, target):
    missing = {target - num for num in preamble}
    for num in preamble:
        if num in missing and num != target - num: 
            return True
    return False
    

def first_invalid():
    numbers = get_input()
    preamble = deque(numbers[:25])
    for i in range(25, len(numbers)):
        current_number = numbers[i]
        if not check_valid(preamble, current_number): 
            return current_number
        preamble.popleft()
        preamble.append(current_number)

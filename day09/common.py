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
    for i in range(25, len(numbers)):
        current_number = numbers[i]
        preamble = numbers[i - 25: i]
        if not check_valid(preamble, current_number): 
            return current_number

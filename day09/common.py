from collections import deque


PREAMBLE_LENGTH = 25


def first_invalid():
    numbers = get_input()
    preamble = deque(numbers[:PREAMBLE_LENGTH])
    for i in range(PREAMBLE_LENGTH, len(numbers)):
        current_number = numbers[i]
        if not check_valid(preamble, current_number): 
            return current_number
        preamble.popleft()
        preamble.append(current_number)


def check_valid(preamble, target):
    # 2-sum problem (see also day01 part1)
    missing = {target - num for num in preamble}
    for num in preamble:
        if num in missing and num != target - num: 
            return True
    return False


def get_input():
    with open("input.txt") as f:
        return [int(line) for line in f.read().splitlines()]

from collections import deque


def get_input():
    with open("input.txt") as f:
        return [int(num) for num in f.read().strip().split(",")]


def nth_number(n):
    starting_numbers = get_input()
    memory = {v:deque([(i+1)], maxlen=2) for i, v in enumerate(starting_numbers)}
    
    last_spoken = starting_numbers[-1]
    for i in range(len(starting_numbers), n):
        turn = i + 1
        if len(memory[last_spoken]) == 2:
            last_spoken = memory[last_spoken][1] - memory[last_spoken][0]
        else:
            last_spoken = 0
        if not last_spoken in memory.keys():
            memory[last_spoken] = deque(maxlen=2)
        memory[last_spoken].append(turn)
    return last_spoken

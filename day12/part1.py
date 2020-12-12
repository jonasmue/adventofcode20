from common import *


def run_instructions(instructions):
    # O(n) time and O(1) space
    current_position = [0, 0]
    current_heading = "E"
    
    for item in instructions:
        operation = item[0]
        arg = item[1]
        if operation in HEADINGS:
            move(current_position, operation, arg)
        elif operation == "F":
            move(current_position, current_heading, arg)
        elif operation == "L":
            next_heading_idx = HEADINGS.index(current_heading) - (arg // 90)
            current_heading = HEADINGS[next_heading_idx]
        elif operation == "R":
            next_heading_idx = HEADINGS.index(current_heading) + (arg // 90)
            current_heading= HEADINGS[next_heading_idx % len(HEADINGS)]
            
    return current_position
            
            
if __name__ == "__main__":
    print(manhattan_distance(run_instructions(get_input())))

from common import *


def run_instructions(instructions):
    # O(n) time and O(1) space
    current_position = [0, 0]
    current_waypoint = [10, 1]
    
    for item in instructions:
        operation = item[0]
        arg = item[1]
        if operation in HEADINGS:
            move(current_waypoint, operation, arg)
        elif operation == "F":
            current_position[0] += arg * current_waypoint[0]
            current_position[1] += arg * current_waypoint[1]
        else:
            rotate_waypoint(current_waypoint, operation, arg)
            
    return current_position


def rotate_waypoint(waypoint, direction, degrees):
    x, y = waypoint[0], waypoint[1]
    if direction == "L":
        while degrees > 0:
            x, y = -y, x
            degrees -= 90
    elif direction == "R":
        while degrees > 0:
            x, y = y, -x
            degrees -= 90
    waypoint[0], waypoint[1] = x, y
    
    
if __name__ == "__main__":
    print(manhattan_distance(run_instructions(get_input())))

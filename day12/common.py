HEADINGS = ["N", "E", "S", "W"]


def get_input():
    with open("input.txt") as f:
        return [(line[0], int(line[1:])) for line in f.read().splitlines()]     
        

def move(point, direction, steps):
    if direction == "N":
        point[1] += steps
    elif direction == "E":
        point[0] += steps
    elif direction == "S":
        point[1] -= steps
    elif direction == "W":
        point[0] -= steps
        

def manhattan_distance(vector):
    return sum([abs(item) for item in vector])

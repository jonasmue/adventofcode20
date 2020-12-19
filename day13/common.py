def get_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        return int(lines[0]), lines[1].split(",")

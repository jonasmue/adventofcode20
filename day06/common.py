def get_input():
  with open("input.txt") as f:
    return [[set(item) for item in group.split()] for group in f.read().split("\n\n")]

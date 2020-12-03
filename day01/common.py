TARGET = 2020

def get_input():
  with open("input.txt") as f:
    return [int(line.strip()) for line in f.readlines()]

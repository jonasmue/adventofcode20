def get_input():
    with open("input.txt") as f:
        return [int(line) for line in f.read().splitlines()]
  
    
def get_sorted_adapters():
    adapters = [0] # jolts of charging outlet
    adapters += sorted(get_input())
    adapters += [adapters[-1] + 3] # jolts of our device
    return adapters

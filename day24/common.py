from collections import defaultdict
from copy import deepcopy


class TileFloor:
    
    def __init__(self):
        self.tiles = defaultdict(bool)
        self.min_x = self.min_y = 0
        self.max_x = self.max_y = 0
        self.black_tiles = 0
        self.initialize_floor(get_input())
        
    def initialize_floor(self, instructions):
        for instruction in instructions:
            x, y = self.get_coordinate(instruction)
            self.min_x = min(self.min_x, x)
            self.min_y = min(self.min_y, y)
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)
            self.tiles[(x,y)] = not self.tiles[(x,y)]
            if self.tiles[(x,y)]: self.black_tiles += 1
            else: self.black_tiles -= 1
        
    def get_coordinate(self, instruction):
        x = y = 0
        i = 0
        while i < len(instruction):
            move = instruction[i]
            i += 1
            if move == "n" or move == "s":
                move += instruction[i]
                i += 1
            if move == "e": 
                x -= 2
            elif move == "se":
                x -= 1
                y -= 1
            elif move == "sw":
                x += 1
                y -= 1
            elif move == "w":
                x += 2
            elif move == "nw":
                x += 1
                y += 1
            elif move == "ne":
                x -= 1
                y += 1
        return x, y
    
    def count_neighbors(self, x, y, snapshot):
        neighbor_coords = [
            (x-2,y), (x-1,y-1), (x+1,y-1),
            (x+2,y), (x+1,y+1), (x-1,y+1)
            ]
        sum = 0
        for c in neighbor_coords:
            if snapshot[c]: sum += 1
        return sum
        
    def run(self, n_rounds=100):
        for _ in range(n_rounds):
            self.min_x -= 2
            self.max_x += 2
            self.min_y -= 1
            self.max_y += 1
            snapshot = deepcopy(self.tiles)
            for x in range(self.min_x, self.max_x + 1):
                for y in range(self.min_y, self.max_y + 1):
                    if y % 2 == 0 and x % 2 != 0: continue
                    if y % 2 != 0 and x % 2 == 0: continue
                    neighbors = self.count_neighbors(x, y, snapshot)
                    black = snapshot[(x,y)]
                    if black and neighbors == 0: 
                        self.tiles[(x,y)] = 0
                        self.black_tiles -= 1
                    if black and neighbors > 2: 
                        self.tiles[(x,y)] = 0
                        self.black_tiles -= 1
                    if not black and neighbors == 2: 
                        self.tiles[(x,y)] = 1
                        self.black_tiles += 1


def get_input():
    with open("input.txt") as f:
        return f.read().splitlines()

from collections import defaultdict
from copy import deepcopy


def get_input():
    with open("input.txt") as f:
        result = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
        active = 0
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                if char == "#":
                    active += 1
                    result[x][y][0][0] = 1
        return result, active
 
     
class ConwayCubes:
    
    def __init__(self, four_dims=False):
        self.cubes, self.active = get_input()
        self.x_range = [0, 8]
        self.y_range = [0, 8]
        self.z_range = [0, 1]
        self.w_range = [0, 1]
        self.four_dims = four_dims
    
    def update_range(self, r):
        r[0], r[1] = r[0] - 1, r[1] + 1
    
    def update_ranges(self):
        ranges = [self.x_range, self.y_range, self.z_range]
        if self.four_dims: ranges.append(self.w_range)
        for r in ranges: self.update_range(r)
        
    def create_snapshot(self):
        return deepcopy(self.cubes)
    
    def get_active_neighbors(self, snapshot, x, y, z, w):
        n = 0
        for x_delta in [-1, 0, 1]:
            for y_delta in [-1, 0, 1]:
                for z_delta in [-1, 0, 1]:
                    for w_delta in [-1, 0, 1]:
                        if x_delta == 0 and y_delta == 0 and z_delta == 0 and w_delta == 0:
                            continue
                        if snapshot[x + x_delta][y + y_delta][z + z_delta][w + w_delta]:
                            n += 1
        return n

    def run(self, cycles=6):
        for _ in range(cycles):
            self.update_ranges()
            snapshot = self.create_snapshot()
            for x in range(self.x_range[0], self.x_range[1]):
                for y in range(self.y_range[0], self.y_range[1]):
                    for z in range(self.z_range[0], self.z_range[1]):
                        for w in range(self.w_range[0], self.w_range[1]):
                            n_active_neighbors = self.get_active_neighbors(snapshot, x, y, z, w)
                            is_active = snapshot[x][y][z][w]
                            if is_active:
                                if n_active_neighbors < 2 or n_active_neighbors > 3:
                                    self.cubes[x][y][z][w] = 0
                                    self.active -= 1
                            else:
                                if n_active_neighbors == 3:
                                    self.cubes[x][y][z][w] = 1
                                    self.active += 1

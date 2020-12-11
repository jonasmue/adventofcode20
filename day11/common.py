def get_input():
    with open("input.txt") as f:
        return [[char for char in line] for line in f.read().splitlines()]

class SeatingSystem:
    def __init__(self, threshold, immediate_neighbors):
        self.state = get_input()
        self.height = len(self.state)
        self.width = len(self.state[0])
        self.occupied = 0
        self.steps = 0
        self.threshold = threshold
        self.immediate_neighbors = immediate_neighbors
    
    def in_bounds(self, row, col):
        if row < 0: return False
        if col < 0: return False
        if row >= self.height: return False
        if col >= self.width: return False
        return True
        
    def create_snapshot(self):
        return [[col for col in self.state[row]] for row in range(len(self.state))]
        
    def occupied_neighbors(self, snapshot, row, col):
        occupied = 0
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                if d_row == 0 and d_col == 0: continue
                check_row = row
                check_col = col
                found_neighbor = False
                while not found_neighbor:
                    check_row -= d_row
                    check_col -= d_col
                    if not self.in_bounds(check_row, check_col): 
                        break
                    elif snapshot[check_row][check_col] == "L": 
                        found_neighbor = True
                    elif snapshot[check_row][check_col] == "#":
                        occupied += 1
                        found_neighbor = True
                    else:
                        found_neighbor = self.immediate_neighbors
        return occupied
    
    def step(self):
        snapshot = self.create_snapshot()
        changed_state = False
        for row in range(self.height):
            for col in range(self.width):
                if self.state[row][col] == ".": continue
                occupied = self.occupied_neighbors(snapshot, row, col)
                if occupied == 0 and self.state[row][col] == "L": 
                    self.state[row][col] = "#"
                    changed_state = True
                    self.occupied += 1
                elif occupied >= self.threshold and self.state[row][col] == "#": 
                    self.state[row][col] = "L"
                    changed_state = True
                    self.occupied -= 1
        return changed_state
        
    def run(self):
        while self.step():
            self.steps += 1

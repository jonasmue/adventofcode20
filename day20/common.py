from collections import Counter
from math import sqrt


class Tile:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.rows = len(self.content)
        self.cols = len(self.content[0])
    
    def cropped_content(self):
        return [row[1:-1] for row in self.content[1:-1]]
        
    def top(self):
        return self.content[0]
        
    def bottom(self):
        return self.content[-1]
        
    def left(self):
        return "".join([row[0] for row in self.content])
        
    def right(self):
        return "".join([row[-1] for row in self.content])
        
    def get_possible_borders(self):
        return [self.top(), self.bottom(), self.left(), self.right(), self.top()[::-1], self.bottom()[::-1], self.left()[::-1], self.right()[::-1]]
        
    def flip_vertical(self):
        self.content = flip_array_vertical(self.content)
        
    def flip_horizontal(self):
        self.content = flip_array_horizontal(self.content)
            
    def rotate_left(self, n_times):
        n_times %= 4
        for _ in range(n_times): self.rotate()
            
    def rotate(self):
        self.content = rotate_array_left(self.content)
        self.rows, self.cols = self.cols, self.rows
             
    def __repr__(self):
        return f"Tile {self.id}"
        
    def __str__(self):
        return f"Tile: {self.id}: {self.content}"
        
        
def get_input():
    with open("input.txt") as f:
        tile_groups = f.read().split("\n\n")
        tiles = []
        for tg in tile_groups:
            lines = tg.splitlines()
            id = int(lines[0][5:9])
            content = lines[1:]
            tiles.append(Tile(id, content))
        return tiles
      
      
def rotate_array_left(array):
    cols = len(array[0])
    result = [""] * cols
    for row in range(len(array)):
        for col, char in enumerate(array[row]):
            result[cols - col - 1] += char
    return result
    
    
def flip_array_horizontal(array):
    return [row[::-1] for row in array]
    
    
def flip_array_vertical(array):
    return array[::-1]
        

def corner_tiles(tiles):
    tile_dict = {tile.id: tile.get_possible_borders() for tile in tiles}
    all_borders = [b for values in tile_dict.values() for b in list(values)]
    border_counter = Counter(all_borders)
    corner_tiles = []
    for tile_id, borders in tile_dict.items():
        border_sum = sum([border_counter[b] for b in borders])
        if border_sum == 12: corner_tiles.append(tile_id)
    return corner_tiles, border_counter

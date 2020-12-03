TREE_CHARACTER = "#"


def trees_for_slope(slope, map):
  trees = 0
  if not len(map): return trees
  height = len(map)
  width = len(map[0])
  
  current_x = 0
  current_y = 0
  
  while current_y < height:
    line = map[current_y]
    if current_x >= width:
      current_x -= width
    if line[current_x] == TREE_CHARACTER:
      trees += 1
    current_x += slope[0]
    current_y += slope[1]
  return trees
  
  
def get_n_trees(slopes):
  # O(slopes * height) time and O(1) space
  trees = 0
  map = get_input()
    
  for slope in slopes:
    slope_trees = trees_for_slope(slope, map)
    if trees == 0: trees = slope_trees
    else: trees *= slope_trees
  return trees
  

def get_input():
  with open("input.txt") as f:
    return f.read().splitlines()

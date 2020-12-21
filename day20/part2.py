from common import *


def align_image_tiles(tiles, top_left_corner, border_counter):
    
    def wanted_tile(current_tile, border):
        for i, tile in enumerate(tiles):
            if border in tile.get_possible_borders():
                if current_tile.id == tile.id: continue
                return tiles.pop(i)
    
    def find_top_left(current_tile):
        top_border = current_tile.bottom()
        tile = wanted_tile(current_tile, top_border)
        border_idx = tile.get_possible_borders().index(top_border)
        if border_idx == 0:
            # Top :)
            pass
        elif border_idx == 1:
            # Bottom
            tile.flip_vertical()
        elif border_idx == 2:
            # Left
            tile.rotate_left(3)
            tile.flip_horizontal()
        elif border_idx == 3:
            # Right
            tile.rotate_left(1)
        elif border_idx == 4:
            # Top Flipped
            tile.flip_horizontal()
        elif border_idx == 5:
            # Bottom Flipped
            tile.rotate_left(2)
        elif border_idx == 6:
            # Left Flipped
            tile.rotate_left(3)
        elif border_idx == 6:
            # Right Flipped
            tile.rotate_left(1)
            tile.flip_horizontal()
        assert(top_border) == tile.top()
        return tile
        
    def find_next_col(current_tile):
        left_border = current_tile.right()
        tile = wanted_tile(current_tile, left_border)
        border_idx = tile.get_possible_borders().index(left_border)
        if border_idx == 0:
            # Top
            tile.rotate_left(1)
            tile.flip_vertical()
        elif border_idx == 1:
            # Bottom
            tile.rotate_left(3)
        elif border_idx == 2:
            # Left :)
            pass
        elif border_idx == 3:
            # Right
            tile.flip_horizontal()
        elif border_idx == 4:
            # Top Flipped
            tile.rotate_left(1)
        elif border_idx == 5:
            # Bottom Flipped
            tile.rotate_left(3)
            tile.flip_vertical()
        elif border_idx == 6:
            # Left Flipped
            tile.flip_vertical()
        elif border_idx == 7:
            # Right Flipped
            tile.rotate_left(2)
        assert(left_border == tile.left())
        return tile
    
    rows = cols = int(sqrt(len(tiles)))
    image = [[None] * cols] * rows
    
    while border_counter[top_left_corner.top()] > 1 or border_counter[top_left_corner.left()] > 1:
        top_left_corner.rotate_left(1)
        
    image = [[top_left_corner]]
    
    for row in range(rows):
        for col in range(cols):
            if row == 0 and col == 0:
                continue
            elif col == 0:
                image.append(list())
                tile = find_top_left(image[row - 1][col])
                image[row].append(tile)
            else: 
                tile = find_next_col(image[row][col - 1])
                image[row].append(tile)
                if row > 0:
                    top_tile = image[row - 1][col]
                    assert(tile.top() == top_tile.bottom())
                    
    assert (len(tiles) == 1 and tiles.pop().id == image[0][0].id)        
    return image
    

def image_tiles_to_image(image_tiles):
    image = []
    for tile_row_idx in range(len(image_tiles)):
        for tile_col_idx in range(len(image_tiles[tile_row_idx])):
            tile = image_tiles[tile_row_idx][tile_col_idx]
            tile_content = tile.cropped_content()
            for content_row_idx, row_content in enumerate(tile_content):
                image_row_idx = tile_row_idx * len(tile_content) + content_row_idx
                if image_row_idx >= len(image): image.append(row_content)
                else: image[image_row_idx] += row_content
    return image


def row_matches_monster(string, offset, indices):
    for idx in indices:
        if string[offset + idx] != "#": return False
    return True
    

def find_sea_monster(image, sea_monster):
    sea_monster_length = max([max(item) for item in sea_monster]) + 1
    sea_monsters = 0
    for row in range(len(image) + 1 - (len(sea_monster))):
        for offset in range(len(image[row]) + 1 - sea_monster_length):
            matches_monster = True
            for i in range(3):
                matches_monster &= row_matches_monster(image[row + i], offset, sea_monster[i])
            if matches_monster: sea_monsters += 1
    return sea_monsters
    

def find_all_sea_monsters(image, sea_monster):
    for _ in range(4):
        found_monsters = find_sea_monster(image, sea_monster)
        if found_monsters: return found_monsters
        image = flip_array_horizontal(image)
        found_monsters = find_sea_monster(image, sea_monster)
        if found_monsters: return found_monsters
        image = rotate_array_left(image)
    return 0
    

def number_of_hashtags(image):
    return sum([row.count("#") for row in image])
    
    
def sea_monster_hashtags(sea_monster, n=1):
    return n * sum([len(row) for row in sea_monster])
    
    
if __name__ == "__main__":
    tiles = get_input()
    corners, border_counter = corner_tiles(tiles)
    top_left_tile = [t for t in tiles if t.id == corners[0]].pop()
    image_tiles = align_image_tiles(tiles, top_left_tile, border_counter)
    image = image_tiles_to_image(image_tiles)
    sea_monster = [[18], [0, 5, 6, 11, 12, 17, 18, 19], [1, 4, 7, 10, 13, 16]]
    n_sea_monsters = find_all_sea_monsters(image, sea_monster)
    print(number_of_hashtags(image) - sea_monster_hashtags(sea_monster, n_sea_monsters))

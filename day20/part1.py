from common import get_input, corner_tiles
from functools import reduce


if __name__ == "__main__":
    corners, _ = corner_tiles(get_input())
    print(reduce(lambda a, b: a * b, corners))

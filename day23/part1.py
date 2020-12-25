from common import *


if __name__ == "__main__":
    game = Game()
    game.play(100)
    print("".join(str(game.val2node[1]).split()[1:]))

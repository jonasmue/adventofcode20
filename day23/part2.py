from common import *


def find_result(val2node):
    one_node = val2node[1]
    factor_1 = one_node.next.value
    factor_2 = one_node.next.next.value
    return factor_1 * factor_2
    

if __name__ == "__main__":
    game = Game(1000000)
    game.play(10000000)
    print(find_result(game.val2node))

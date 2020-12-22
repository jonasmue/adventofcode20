from common import *


if __name__ == "__main__":
    _, winning_deck = play_game(*get_input())
    print(calculate_score(winning_deck))

from collections import deque


def get_input():
    with open("input.txt") as f:
        groups = f.read().split("\n\n")
        player_1 = deque([int(line) for line in groups[0].splitlines()[1:]])
        player_2 = deque([int(line) for line in groups[1].splitlines()[1:]])
        return player_1, player_2


def calculate_score(deck):
    score = 0
    while len(deck): score += len(deck) * deck.popleft()
    return score
    
    
def play_game(player_1, player_2, recursive=False):
    history = set()
    while len(player_1) and len(player_2):
        state_1, state_2 = tuple(player_1), tuple(player_2)
        if state_1 in history and state_2 in history: 
            return 0, player_1
        history.add(state_1)
        history.add(state_2)
        
        card_1, card_2 = player_1.popleft(), player_2.popleft()
        l_1, l_2 = len(player_1), len(player_2)
        if recursive and card_1 <= l_1 and card_2 <= l_2:
            p1 = deque(list(player_1)[:card_1])
            p2 = deque(list(player_2)[:card_2])
            if play_game(p1, p2, True)[0] == 0:
                player_1.extend([card_1, card_2])
            else:
                player_2.extend([card_2, card_1])
                
        elif card_1 > card_2:
            player_1.extend([card_1, card_2])
        else:
            player_2.extend([card_2, card_1])
            
    return (0, player_1) if len(player_1) else (1, player_2)

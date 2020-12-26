from common import *


if __name__ == "__main__":
    card_pub_key, door_pub_key = get_input()
    card_loop_size = get_loop_size(card_pub_key)
    door_loop_size = get_loop_size(door_pub_key)
    
    encryption_key_card = encryption_key(door_pub_key, card_loop_size)
    encryption_key_door = encryption_key(card_pub_key, door_loop_size)
        
    assert(encryption_key_card == encryption_key_door)
    print(encryption_key_card)

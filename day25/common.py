def get_input():
    with open("input.txt") as f:
        card_pub_key, door_pub_key = f.read().splitlines()
    return int(card_pub_key), int(door_pub_key)


def transform(value, subject_number):
    return (value * subject_number) % 20201227


def get_loop_size(pub_key):
    value = 1
    loop_size = 0
    while True:
        loop_size += 1
        value = transform(value, 7)
        if value == pub_key:
            return loop_size

                      
def encryption_key(other_pub_key, loop_size):
    key = 1
    for _ in range(loop_size):
        key = transform(key, other_pub_key)
    return key

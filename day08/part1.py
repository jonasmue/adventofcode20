from common import *


def find_loop():
    # O(n) time and space
    computer = Computer(get_input())
    computer.run()
    return computer.accumulator
    

if __name__ == "__main__":
    print(find_loop())

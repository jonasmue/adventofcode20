from tqdm import tqdm

      
def get_input():
    with open("input.txt") as f:
        return [int(char) for char in f.read().strip()]
                  

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.destination = None
        
    def __repr__(self):
        start = self.value
        result = ""
        node = self
        first = True
        while node is not None:
            if first: first = False
            elif node.value == start: break
            result += f"{node.value} "
            node = node.next
        return result


class Game:
    
    def __init__(self, up_to=0):
        self.val2node = {}
        inpt = get_input()
        self.start = Node(inpt[0])
        current_node = self.start
        self.val2node[current_node.value] = current_node 
        for item in inpt[1:]:
            current_node.next = Node(item)
            current_node = current_node.next
            self.val2node[item] = current_node
        current_node.next = self.start
        self.max_value = max(self.val2node.keys())
        self.min_value = min(self.val2node.keys())
        if up_to > self.max_value:
            last_node = current_node
            for i in range(self.max_value + 1, up_to + 1):
                last_node.next = Node(i)
                last_node = last_node.next
                self.val2node[i] = last_node
            last_node.next = self.start
        self.max_value = max(self.val2node.keys())
        
    def find_destination(self, cup, picked):
        desired = cup.value
        while True:
           desired -= 1
           if desired not in picked:
               if desired >= self.min_value:
                   return self.val2node[desired]
               else:
                   desired = self.max_value + 1

    def play(self, moves):
        current_cup = self.start
        for i in tqdm(range(moves)):
            # 1. Pick up 3 cups
            first = current_cup.next
            second = first.next
            third = second.next
            # 2. Remove them
            new_next = third.next
            current_cup.next = new_next
            # 3. Find destination cup
            picked_values = {first.value, second.value, third.value}
            destination = self.find_destination(current_cup, picked_values)
            # 4. Insert 3 cups
            dest_next = destination.next
            destination.next = first
            third.next = dest_next
            # 5. Move current_cup
            current_cup = new_next

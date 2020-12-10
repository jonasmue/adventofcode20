from common import get_sorted_adapters


def difference_product():
    # Sorting (next line) takes O(nlogn) time and O(n) space
    adapters = get_sorted_adapters()
    
    # Rest of the algorithm:
    # O(n) time and O(1) space
    one_diff = 0
    three_diff = 0
    for i in range(1, len(adapters)):
        current_adapter = adapters[i]
        prev_adapter = adapters[i-1]
        difference = current_adapter - prev_adapter
        if difference == 1: one_diff += 1
        if difference == 3: three_diff += 1
    return one_diff * three_diff
    
    
if __name__ == "__main__":
    print(difference_product())

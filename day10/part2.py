from common import get_sorted_adapters
from collections import deque


def count_ways():
    # Sorting (next line) takes O(nlogn) time and O(n) space
    adapters = get_sorted_adapters()
    
    # Rest of the algorithm:
    # O(n) time and O(1) space
    dp = deque([1, 1, 1], maxlen=3)
    for i in range(len(adapters)):
        current_adapter = adapters[i]
        current_ways = dp[-1]
        if i >= 2 and adapters[i - 2] == current_adapter - 2:
            current_ways += dp[1]
        if i >= 3 and adapters[i - 3] == current_adapter - 3:
            current_ways += dp[0]
        dp.append(current_ways)
            
    return dp[-1]


if __name__ == "__main__":
    print(count_ways())

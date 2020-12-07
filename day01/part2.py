from common import *


def find_result(numbers):
    # 3-sum in O(n^2) time and O(1) space
    numbers = sorted(numbers)
    for i, first in enumerate(numbers):
        l = i + 1
        r = len(numbers) - 1
        while l < r:
            left = numbers[l]
            right = numbers[r]

            sum = first + left + right
            if sum == TARGET:
                return first * left * right
            elif sum < TARGET:
                l += 1
            else:
                r -= 1


if __name__ == "__main__":
    numbers = get_input()
    result = find_result(numbers)
    print(result)

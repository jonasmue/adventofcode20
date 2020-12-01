from common import *

def find_result(numbers):
	# Classic 3-sum problem
	numbers = sorted(numbers)
	for i, first in enumerate(numbers):
		l = i + 1
		r = len(numbers) - 1
		while l < r:
			left = numbers[l]
			right = numbers[r]
			
			sum = first + left + right
			if sum == 2020: return first * left * right
			elif sum < 2020: l += 1
			else: r -= 1
		

if __name__ == "__main__":
	numbers = get_input()
	result = find_result(numbers)
	print(result)

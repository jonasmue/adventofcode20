from common import *

def find_result(numbers):
	# 2-sum in O(n) time and space
	wanted_numbers = set()
	for n in numbers:
		delta = TARGET - n
		if n in wanted_numbers:
			return n * delta
		wanted_numbers.add(delta)
	

if __name__ == "__main__":
	numbers = get_input()
	result = find_result(numbers)
	print(result)

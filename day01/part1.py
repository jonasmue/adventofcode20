def get_input():
	with open("input.txt") as f:
		return [int(line.strip()) for line in f.readlines()]
	
	
def find_result(numbers):
	wanted_numbers = set()
	for n in numbers:
		delta = 2020 - n
		if n in wanted_numbers:
			return n * delta
		wanted_numbers.add(delta)
	

if __name__ == "__main__":
	numbers = get_input()
	result = find_result(numbers)
	print(result)

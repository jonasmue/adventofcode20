class PasswordPolicy:
	def __init__(self, character, firstValue, secondValue):
		self.character = character
		self.firstValue = firstValue
		self.secondValue = secondValue
		
	def __repr__(self):
		return "{} - {} {}".format(self.firstValue, self.secondValue, self.character)
		
		
def count_valid(policyFunction):
	return sum(map(policyFunction, get_input()))


def get_input():
	result = []
	with open("input.txt") as f:
		for line in f.readlines():
			split = line.split()
			assert len(split) == 3
			
			policy_values = split[0].split("-")
			assert len(policy_values) == 2
			character = split[1][0]
			policy = PasswordPolicy(character, int(policy_values[0]), int(policy_values[1]))
			password = split[2]
			
			result.append((policy, password))
			
		return result

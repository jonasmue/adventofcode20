from common import count_valid

def policy_function(policy, password):
	# O(np) time and O(1) space
	# where n: number of passwords, p: length of longest password
	char_count = password.count(policy.character)
	return char_count >= policy.firstValue and char_count <= policy.secondValue

if __name__ == "__main__":
	print(count_valid(policy_function))

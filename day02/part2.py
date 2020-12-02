from common import count_valid

def policy_function(policy, password):
	# O(n) time and O(1) space
	if len(password) < policy.secondValue: return False
	match_first = password[policy.firstValue - 1] == policy.character
	match_second = password[policy.secondValue - 1] == policy.character
	return match_first ^ match_second

if __name__ == "__main__":
	print(count_valid(policy_function))

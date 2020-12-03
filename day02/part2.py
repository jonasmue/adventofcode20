from common import count_valid

def policy_function(policy_tuple):
  # O(n) time and O(1) space
  policy, password = policy_tuple
  if len(password) < policy.second_value: return False
  match_first = password[policy.first_value - 1] == policy.character
  match_second = password[policy.second_value - 1] == policy.character
  return match_first ^ match_second


if __name__ == "__main__":
  print(count_valid(policy_function))

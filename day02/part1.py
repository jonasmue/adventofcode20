from common import count_valid


def policy_function(policy_tuple):
    # O(np) time and O(1) space
    # where n: number of passwords, p: length of longest password
    policy, password = policy_tuple
    char_count = password.count(policy.character)
    return char_count >= policy.first_value and char_count <= policy.second_value


if __name__ == "__main__":
    print(count_valid(policy_function))

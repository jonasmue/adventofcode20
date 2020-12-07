class PasswordPolicy:
    def __init__(self, character, first_value, second_value):
        self.character = character
        self.first_value = first_value
        self.second_value = second_value

    def __repr__(self):
        return "{} - {} {}".format(self.first_value, self.second_value, self.character)


def count_valid(policy_function):
    return sum(map(policy_function, get_input()))


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

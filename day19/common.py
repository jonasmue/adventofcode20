import regex


def get_input():
    with open("input.txt") as f:
        groups = f.read().split("\n\n")
        rules = {}
        for line in groups[0].splitlines():
            split = line.split(":")
            rule = split[0]
            if "|" in line:
                rules[rule] = [subrule.strip().split() for subrule in split[1].split("|")]
            else:
                rules[rule] = [split[1].strip().split()]
        messages = groups[1].splitlines()
        return rules, messages
        

def expand_rules(rules, rule="0"):
    subrules = rules[rule]
    return "(" + "|".join(["".join([expand_rules(subrule) if subrule.isnumeric() else subrule for subrule in part]) for part in subrules]) + ")"


def run(rules, messages):
    pattern = expand_rules(rules) + "$"
    return sum([bool(regex.match(pattern, message)) for message in messages])

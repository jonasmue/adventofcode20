from common import *


if __name__ == "__main__":
    rules, messages = get_input()
    rules["8"] = [["42", "+"]]
    rules["11"] = [[f'(?P<rule11>{expand_rules(rules, "42")}(?&rule11)?{expand_rules(rules, "31")})']]
    print(run(rules, messages))

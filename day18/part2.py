from common import *


if __name__ == "__main__":
    op = {"+": 2, "*": 1}
    print(sum([evaluate(rpn(term, op), op) for term in get_input()]))

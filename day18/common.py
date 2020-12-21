def get_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def evaluate(rpn, operators):
    num_stack = []
    for token in rpn:
        if token in operators.keys():
            arg_2 = num_stack.pop()
            if token == "+":
                num_stack[-1] += arg_2
            elif token == "*":
                num_stack[-1] *= arg_2
        else:
            num_stack.append(token)
    return num_stack.pop()


def rpn(term, operators):
    output_queue = []
    op_stack = []
    for token in term:
        if token.isnumeric():
            output_queue.append(int(token))
        elif token in operators.keys():
            precedence = operators[token]
            while len(op_stack) and op_stack[-1] != "(" and operators[op_stack[-1]] >= precedence:
                output_queue.append(op_stack.pop())
            op_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack[-1] != "(":
                output_queue.append(op_stack.pop())
            op_stack.pop()
            
    while len(op_stack):
        output_queue.append(op_stack.pop())
        
    return output_queue

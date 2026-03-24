def f(tokens):
    stack = []
    n = len(tokens)
    for i in range(n):
        if tokens[i] not in "+-*/":
            stack.append(tokens[i])
        else:
            if len(stack) >= 2:
                x1 = stack.pop()
                x2 = stack.pop()
                if tokens[i] == "+":
                    res = (int(x1) + int(x2))
                    stack.append(res)
                elif tokens[i] == "-":
                    res = (int(x2) - int(x1))
                    stack.append(res)
                elif tokens[i] == "*":
                    res = (int(x1) * int(x2))
                    stack.append(res)
                else:
                    res = int(int(x2) / int(x1))
                    stack.append(res)
    return int(stack.pop())
def f(s):
    d = {')': '(', ']': '[', '}': '{'}
    stack = []
    for znak in s:
        if znak in d.values():
            stack.append(znak)
        else:
            if not stack or stack.pop() != d[znak]:
                return False
    return not stack
s = "([])"
print(f(s))
def bitgame(T):
    stack = []
    for x in T:
        czy_kolizja = False
        while stack and stack[-1] <= x:
            stack.pop()
            czy_kolizja = True
        if czy_kolizja == False:
            stack.append(x)
    return len(stack)
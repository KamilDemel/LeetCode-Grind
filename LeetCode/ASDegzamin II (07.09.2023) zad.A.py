def dominance_brute(P):
    T = [0 for _ in range(len(P))]
    for i in range(len(P)):
        for j in range(len(P)):
            x_i,y_i = P[i]
            x_j,y_j = P[j]
            if x_i == x_j and y_i == y_j:
                continue
            if x_i > x_j and y_i > y_j:
                T[i] += 1
    return max(T)
def dominance(P):
    Tx = [0 for _ in range(len(P) + 2)]
    Ty = [0 for _ in range(len(P) + 2)]
    count_x = [0] * (len(P) + 2)
    count_y = [0] * (len(P) + 2)
    for x,y in P:
        count_x[x] += 1
        count_y[y] += 1
    for i in range(len(P),0,-1):
        Tx[i] = Tx[i+1] + count_x[i]
        Ty[i] = Ty[i+1] + count_y[i]
    res = 0
    for x,y in P:
        res = max(res,len(P) - Tx[x] - Ty[y] + 1)
    return res

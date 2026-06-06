import collections
def sol(n,L):
    adj_list = [[] for _ in range(n)]
    in_degree = [0] * n
    for p,q in L:
        adj_list[q].append(p)
        in_degree[p] += 1
    kolejka = collections.deque()
    for i in range(n):
        if in_degree[i] == 0:
            kolejka.append(i)
    time = 0
    while kolejka:
        time += 1
        for _ in range(len(kolejka)):
            curr_idx_zadanie = kolejka.popleft()
            for sasiad in adj_list[curr_idx_zadanie]:
                in_degree[sasiad] -= 1
                if in_degree[sasiad] == 0:
                    kolejka.append(sasiad)
    return time





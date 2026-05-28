import collections
def kingnqueen(V,E,D, K,Q,B):
    adj_list = [[] for _ in range(V)]
    for u,v in E:
        adj_list[u].append(v)
        adj_list[v].append(u)
    ctr = 0
    for i in range(D):
        visited = set()
        kolejka = collections.deque()
        kolejka.append(K[i])
        visited.add(K[i])
        while kolejka:
            curr_V = kolejka.popleft()
            if curr_V == Q[i]:
                ctr += 1
                break
            for sasiad in adj_list[curr_V]:
                if sasiad == B[i]:
                    continue
                if sasiad not in visited:
                    visited.add(sasiad)
                    kolejka.append(sasiad)
    return ctr

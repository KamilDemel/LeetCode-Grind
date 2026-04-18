import collections
def solution(n,edges):
    adj_list = [[] for _ in range(n)]
    for p, q in edges:
        adj_list[p].append(q)
        adj_list[q].append(p)
    visited = set()
    ctr = 0
    for i in range(len(adj_list)):
        if i in visited:
            continue
        visited.add(i)
        kolejka = collections.deque()
        kolejka.append(i)
        while kolejka:
            curr_i = kolejka.popleft()
            for node in adj_list[curr_i]:
                if node not in visited:
                    visited.add(node)
                    kolejka.append(node)
        ctr += 1
    return ctr

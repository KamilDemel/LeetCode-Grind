import collections
def solution(n,edges):
    adj_list = [[] for _ in range(n)]
    if len(edges) != n - 1:
        return False
    for p,q in edges:
        adj_list[p].append(q)
        adj_list[q].append(p)
    start_point = 0
    visited = set()
    kolejka = collections.deque()
    visited.add(start_point)
    kolejka.append(start_point)
    while kolejka:
        curr_i = kolejka.popleft()
        for k in range(len(adj_list[curr_i])):
            if adj_list[curr_i][k] not in visited:
                visited.add(adj_list[curr_i][k])
                kolejka.append(adj_list[curr_i][k])
    if len(visited) == n:
        return True
    return False
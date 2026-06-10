import collections
def critical(V, E):
    adj_list = [[] for _ in range(V)]
    for u, v in E:
        adj_list[u].append(v)
    ile_krytycznych = 0
    for blocked_u, blocked_v in E:
        visited = [False] * V
        visited[blocked_u] = True
        kolejka = collections.deque([blocked_u])
        reachable = False
        while kolejka and not reachable:
            curr_v = kolejka.popleft()
            for sasiedzi in adj_list[curr_v]:
                if curr_v == blocked_u and sasiedzi == blocked_v:
                    continue
                if not visited[sasiedzi]:
                    if sasiedzi == blocked_v:
                        reachable = True
                        break
                    visited[sasiedzi] = True
                    kolejka.append(sasiedzi)
        if not reachable:
            ile_krytycznych += 1
    return ile_krytycznych
import heapq
def sol(n, roads):
    adj_list = [[] for _ in range(n)]
    for u, v, time in roads:
        adj_list[u].append((time, v))
        adj_list[v].append((time, u))
    print(adj_list)
    distances = [float("inf")] * n
    distances[0] = 0
    ways = [0] * n
    ways[0] = 1
    pq = [(0, 0)]
    while pq:
        curr_time, curr_node = heapq.heappop(pq)
        if curr_time > distances[curr_node]:
            continue
        for czas, sasiad in adj_list[curr_node]:
            new_time = curr_time + czas
            if new_time < distances[sasiad]:
                distances[sasiad] = new_time
                ways[sasiad] = ways[curr_node]
                heapq.heappush(pq, (new_time, sasiad))
            elif new_time == distances[sasiad]:
                ways[sasiad] += ways[curr_node]
    return ways[n-1] % (10**9 + 7)
    """
    ctr = 0
    visited = set()
    visited.add(0)
    def dfs(node=0,best_czas=0):
        nonlocal ctr
        if best_czas > best_time:
            return
        if node == n - 1:
            if best_czas == best_time:
                ctr += 1
        for czas, sasiad in adj_list[node]:
            if sasiad not in visited:
                visited.add(sasiad)
                dfs(sasiad,best_czas+czas)
                visited.remove(sasiad)
    dfs()
    return ctr
    """
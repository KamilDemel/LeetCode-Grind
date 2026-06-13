import heapq
import math
def maxProbability(n, edges, succProb, start_node, end_node):
    graph = []
    for krawedz, time in zip(edges,succProb):
        u,v = krawedz
        graph.append((u,v,time))
    adj_list = [[] for _ in range(n)]
    for u, v, time in graph:
        adj_list[u].append((time, v))
        adj_list[v].append((time, u))
    distances = [float("inf")] * n
    distances[start_node] = 0.0
    pq = [(0.0, start_node)]
    while pq:
        curr_time, curr_node = heapq.heappop(pq)
        if curr_time > distances[curr_node]:
            continue
        for czas, sasiad in adj_list[curr_node]:
            if czas == 0.0:
                continue
            new_time = curr_time + (-math.log(czas))
            if new_time < distances[sasiad]:
                distances[sasiad] = new_time
                heapq.heappush(pq, (new_time, sasiad))
    if distances[end_node] == float("inf"):
        return 0
    return math.exp(-distances[end_node])
import heapq
def warrior(G, s, t):
    V = max((max(u,v) for u,v,w in G)) + 1
    adj_list = [[] for _ in range(V)]
    for u,v,w in G:
        adj_list[u].append((w,v))
        adj_list[v].append((w,u))
    print(adj_list)
    distances = [float("inf")] * V
    start_point = s
    pq = [(0,start_point,0)]
    distances[start_point] = 0
    while pq:
        curr_weight, curr_node,zmeczenie = heapq.heappop(pq)
        if curr_weight > distances[curr_node]:
            continue
        for waga,wezel in adj_list[curr_node]:
            if zmeczenie + waga > 16:
                nowy_czas = curr_weight + waga + 8
                nowe_zmeczenie = waga
            else:
                nowy_czas = curr_weight + waga
                nowe_zmeczenie = zmeczenie + waga
            if nowy_czas < distances[wezel]:
                distances[wezel] = nowy_czas
                heapq.heappush(pq,(nowy_czas,wezel,nowe_zmeczenie))
    return distances[t]

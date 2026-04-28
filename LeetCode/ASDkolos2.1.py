import heapq
def lets_roll(start_city, flights, resorts):
    V = max(max(u, v) for u, v, w in flights) + 1
    adj_list = [[] for _ in range(V)]
    for u,v,w in flights:
        adj_list[u].append((w,v))
        adj_list[v].append((w,u))
    distances = [float("inf")] * V
    distances[start_city] = 0
    pq = [(0,start_city)]
    visited = set()
    laczny_koszt = 0
    while pq:
        curr_distance, curr_node = heapq.heappop(pq)
        if curr_distance > distances[curr_node]:
            continue
        if curr_node in visited:
            continue
        visited.add(curr_node)
        if curr_node in resorts:
            laczny_koszt += curr_distance * 2
            continue
        for sasiedzi in adj_list[curr_node]:
            waga,node = sasiedzi
            if node not in visited:
                nowy_dystans = curr_distance + waga
                if nowy_dystans < distances[node]:
                    distances[node] = nowy_dystans
                    heapq.heappush(pq,(nowy_dystans,node))
    return laczny_koszt

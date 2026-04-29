import heapq
def sol(G,s,t):
    V = max(max(u,v) for u,v,w in G) + 1
    adj_list = [[] for _ in range(V)]
    for u,v,w in G:
        adj_list[u].append((w,v))
        adj_list[v].append((w,u))
    print(adj_list)
    distances = [[float("inf"),float("inf")] for _ in range(V)]
    start_point = s
    pq = [(0,start_point,0),(0,start_point,1)]
    distances[start_point][0] = 0
    distances[start_point][1] = 0
    while pq:
        curr_waga, curr_node, kto_prowadzi = heapq.heappop(pq)
        if curr_waga > distances[curr_node][kto_prowadzi]:
            continue
        for waga,sasiad in adj_list[curr_node]:
            if kto_prowadzi == 1:
                waga = 0
            nowy_dystans = waga + curr_waga
            if nowy_dystans < distances[sasiad][1-kto_prowadzi]:
                distances[sasiad][1-kto_prowadzi] = nowy_dystans
                heapq.heappush(pq,(nowy_dystans,sasiad,1-kto_prowadzi))
    return min(distances[t][0],distances[t][1])


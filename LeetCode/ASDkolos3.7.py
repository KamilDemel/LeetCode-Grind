import heapq
def start_travel(n,E,S,a,b):
    adj_list = [[] for _ in range(n+1)]
    for u,v,czas in E:
        adj_list[u].append((czas,v))
        adj_list[v].append((czas,u))
    for i in S:
        adj_list[n].append((0,i))
        adj_list[i].append((0,n))
    distances = [float("inf")] * (n+1)
    distances[a] = 0
    pq = [(0,a)]
    while pq:
        curr_czas, curr_v = heapq.heappop(pq)
        if curr_czas > distances[curr_v]:
            continue
        for ob_czas, sasiad in adj_list[curr_v]:
            new_czas = ob_czas + curr_czas
            if new_czas < distances[sasiad]:
                distances[sasiad] = new_czas
                heapq.heappush(pq,(new_czas,sasiad))
    return distances[b]


import heapq
def solution(times,n,k):
    adj_list = [[] for _ in range(n+1)]
    distances = [float("inf")] * (n+1)
    distances[k] = 0
    for u,v,w in times:
        adj_list[u].append((w,v))
    pq = [(0,k)]
    while pq:
        curr_distance, curr_node = heapq.heappop(pq)
        if curr_distance > distances[curr_node]:
            continue
        for waga, sasiad in adj_list[curr_node]:
            nowy_dystans = curr_distance + waga
            if nowy_dystans < distances[sasiad]:
                distances[sasiad] = nowy_dystans
                heapq.heappush(pq,(nowy_dystans,sasiad))
    if max(distances[1:]) == float("inf"):
        return -1
    else:
        return max(distances[1:])
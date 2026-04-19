import heapq
def solution(n,flights,src,dst,k):
    adj_list = [[] for _ in range(n)]
    for z,do,cena in flights:
        adj_list[z].append((cena,do))
    min_przesiadki = [float("inf")] * n
    pq = [(0,src,0)]
    while pq:
        curr_distance, curr_node,ctr = heapq.heappop(pq)
        if curr_node == dst:
            return curr_distance
        if ctr >= min_przesiadki[curr_node]:
            continue
        min_przesiadki[curr_node] = ctr
        for waga,sasiedzi in adj_list[curr_node]:
            nowy_dystans = curr_distance + waga
            if ctr <= k:
                heapq.heappush(pq,(nowy_dystans,sasiedzi,ctr+1))
    return -1
import heapq
def goodknight(G,s,t):
    V = len(G)
    adj_list = [[] for _ in range(V)]
    for i in range(V):
        for j in range(len(G[0])):
            if G[i][j] == -1:
                continue
            adj_list[i].append((G[i][j],j))
    distances = [[float("inf") for _ in range(V)] for _ in range(17)]
    distances[0][s] = 0
    pq = [(0,s,0)]
    while pq:
        curr_czas, curr_v, ile_bez_nocowania = heapq.heappop(pq)
        if curr_czas > distances[ile_bez_nocowania][curr_v]:
            continue
        for waga, sasiad in adj_list[curr_v]:
            if ile_bez_nocowania + waga <= 16:
                new_czas = curr_czas + waga
                if new_czas < distances[ile_bez_nocowania + waga][sasiad]:
                    distances[ile_bez_nocowania+ waga][sasiad] = new_czas
                    heapq.heappush(pq,(new_czas,sasiad,ile_bez_nocowania + waga))
            new_czas_ze_spaniem = curr_czas + waga + 8
            if new_czas_ze_spaniem < distances[waga][sasiad]:
                distances[waga][sasiad] = new_czas_ze_spaniem
                heapq.heappush(pq,(new_czas_ze_spaniem,sasiad,waga))
    ans = float("inf")
    for i in range(17):
        ans = min(ans,distances[i][t])
    return ans
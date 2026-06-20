import heapq
"""
def armstrong(B, G, s, t):
    max_V = max(max(u,v) for u,v,w in G)
    adj_list = [[] for _ in range(max_V + 1)]
    for u,v,w in G:
        adj_list[u].append((w,v))
        adj_list[v].append((w,u))
    wyniki = []
    for idx_roweru, p, q in B:
        distances = [[float("inf")] * (max_V + 1) for _ in range(2)]
        distances[0][s] = 0
        distances[1][s] = 0
        pq = [(0, s, 1.0,0)]
        mnoznik = p/q
        if mnoznik >= 1:
            continue
        while pq:
            curr_distance, curr_v, curr_mnoznik, czy_uzyto_roweru = heapq.heappop(pq)
            if curr_distance > distances[czy_uzyto_roweru][curr_v]:
                continue
            for waga_sasiada, sasiad in adj_list[curr_v]:
                new_distans = (waga_sasiada * curr_mnoznik) + curr_distance
                if sasiad == idx_roweru and czy_uzyto_roweru == 0:
                    nowy_stan = 1
                    if new_distans < distances[nowy_stan][sasiad]:
                        distances[nowy_stan][sasiad] = new_distans
                        heapq.heappush(pq, (new_distans, sasiad, mnoznik, nowy_stan))
                else:
                    if new_distans < distances[czy_uzyto_roweru][sasiad]:
                        distances[czy_uzyto_roweru][sasiad] = new_distans
                        heapq.heappush(pq, (new_distans, sasiad, curr_mnoznik, czy_uzyto_roweru))
        wyniki.append(distances[0][t])
        wyniki.append(distances[1][t])
    return min(wyniki)
"""
def armstrong(B,G,s,t):
    max_V = max(max(u,v) for u,v,w in G)
    adj_list = [[] for _ in range(max_V + 1)]
    for u,v,w in G:
        adj_list[u].append((w,v))
        adj_list[v].append((w,u))
    distances_od_s = [float("inf")] * (max_V + 1)
    distances_od_t = [float("inf")] * (max_V + 1)
    distances_od_s[s] = 0
    distances_od_t[t] = 0
    pq1 = [(0,s)]
    while pq1:
        curr_distance, curr_v = heapq.heappop(pq1)
        if curr_distance > distances_od_s[curr_v]:
            continue
        for waga, sasiad in adj_list[curr_v]:
            new_distanc = waga + curr_distance
            if new_distanc < distances_od_s[sasiad]:
                distances_od_s[sasiad] = new_distanc
                heapq.heappush(pq1,(new_distanc,sasiad))
    pq2 = [(0,t)]
    while pq2:
        curr_distance, curr_v = heapq.heappop(pq2)
        if curr_distance > distances_od_t[curr_v]:
            continue
        for waga, sasiad in adj_list[curr_v]:
            new_distanc = waga + curr_distance
            if new_distanc < distances_od_t[sasiad]:
                distances_od_t[sasiad] = new_distanc
                heapq.heappush(pq2,(new_distanc,sasiad))
    best_czas = distances_od_s[t]
    for idx_v,p,q in B:
        czas = distances_od_s[idx_v] + (distances_od_t[idx_v] * (p/q))
        best_czas = min(best_czas,czas)
    return best_czas

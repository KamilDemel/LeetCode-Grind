import heapq
def sol(G,C,D,s,t):
    start_point = s
    V = len(C)
    adj_list = [[] for _ in range(V)]
    for u,v,w in G:
        adj_list[u].append((w,v))
        adj_list[v].append((w,u))
    koszta = [[float("inf") for _ in range(D+1)] for _ in range(V)]
    koszta[start_point][0] = 0
    pq = [(0,start_point,0)]
    while pq:
        obecny_koszt,curr_node,pojemnosc_baku = heapq.heappop(pq)
        if obecny_koszt > koszta[curr_node][pojemnosc_baku]:
            continue
        if pojemnosc_baku < D:
            new_koszt = obecny_koszt + C[curr_node]
            if new_koszt < koszta[curr_node][pojemnosc_baku+1]:
                koszta[curr_node][pojemnosc_baku+1] = new_koszt
                heapq.heappush(pq,(new_koszt,curr_node,pojemnosc_baku+1))
        for waga_krawedzi,sasiad in adj_list[curr_node]:
            if pojemnosc_baku >= waga_krawedzi:
                if obecny_koszt < koszta[sasiad][pojemnosc_baku-waga_krawedzi]:
                    koszta[sasiad][pojemnosc_baku-waga_krawedzi] = obecny_koszt
                    heapq.heappush(pq,(obecny_koszt,sasiad,pojemnosc_baku-waga_krawedzi))
    return min(koszta[t])



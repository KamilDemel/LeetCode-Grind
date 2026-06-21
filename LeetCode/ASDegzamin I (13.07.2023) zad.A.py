import heapq
def gold(G,V,s,t,r):
    num_V = len(V)
    best_wynik = float("inf")
    for i in range(len(V)):
        distances = [[float("inf")] * 2 for _ in range(num_V)]
        distances[s][0] = 0
        pq = [(0,s,0)]
        while pq:
            curr_koszt, curr_v, czy_obrabowana = heapq.heappop(pq)
            if curr_v == i and czy_obrabowana == 0:
                koszt_po_napadzie = curr_koszt - V[i]
                if koszt_po_napadzie < distances[curr_v][1]:
                    distances[curr_v][1] = koszt_po_napadzie
                    heapq.heappush(pq, (koszt_po_napadzie, curr_v, 1))
            if curr_koszt > distances[curr_v][czy_obrabowana]:
                continue
            for sasiad, koszt in G[curr_v]:
                if czy_obrabowana == 1:
                    new_dystans = (2 * koszt + r) + curr_koszt
                    if new_dystans < distances[sasiad][1]:
                        distances[sasiad][1] = new_dystans
                        heapq.heappush(pq,(new_dystans,sasiad,czy_obrabowana))
                if czy_obrabowana == 0:
                    nowy_dystans = koszt + curr_koszt
                    if nowy_dystans < distances[sasiad][0]:
                        distances[sasiad][0] = nowy_dystans
                        heapq.heappush(pq,(nowy_dystans,sasiad, czy_obrabowana))
        if min(distances[t][0],distances[t][1]) < best_wynik:
            best_wynik = min(distances[t][0],distances[t][1])
    return best_wynik

def gold_v2(G, V, s, t, r):
    num_V = len(V)
    distances = [[float("inf")] * 2 for _ in range(num_V)]
    distances[s][0] = 0
    pq = [(0, s, 0)]
    while pq:
        curr_koszt, curr_v, stan = heapq.heappop(pq)
        if curr_koszt > distances[curr_v][stan]:
            continue
        for sasiad, koszt in G[curr_v]:
            if stan == 0:
                nowy_dystans_czysty = curr_koszt + koszt
                if nowy_dystans_czysty < distances[sasiad][0]:
                    distances[sasiad][0] = nowy_dystans_czysty
                    heapq.heappush(pq, (nowy_dystans_czysty, sasiad, 0))
                koszt_ucieczki = curr_koszt - V[curr_v] + (2 * koszt + r)
                if koszt_ucieczki < distances[sasiad][1]:
                    distances[sasiad][1] = koszt_ucieczki
                    heapq.heappush(pq, (koszt_ucieczki, sasiad, 1))
            elif stan == 1:
                nowy_dystans_scigany = curr_koszt + (2 * koszt + r)
                if nowy_dystans_scigany < distances[sasiad][1]:
                    distances[sasiad][1] = nowy_dystans_scigany
                    heapq.heappush(pq, (nowy_dystans_scigany, sasiad, 1))
    return min(distances[t][0], distances[t][1], distances[t][0] - V[t])
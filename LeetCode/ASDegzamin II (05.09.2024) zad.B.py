import heapq
def sol(E,B,A):
    V_max = max(max(u,v) for u,v,czas,typ in E)
    adj_list = [[] for _ in range(V_max + 1)]
    for u,v,czass,typp in E:
        if typp == "P":
            adj_list[u].append((czass,v,0))
            adj_list[v].append((czass,u,0))
        else:
            adj_list[u].append((czass, v, 1))
            adj_list[v].append((czass, u, 1))
    distances = [[float("inf")] * (V_max+1) for _ in range(4)]
    distances[3][A] = 0
    pq = [(0,A,3)]
    print(adj_list)
    while pq:
        curr_czas, curr_v, curr_rozklad = heapq.heappop(pq)
        if curr_czas > distances[curr_rozklad][curr_v]:
            continue
        for czas,sasiad,rozklad in adj_list[curr_v]:
            if curr_rozklad == 3:
                new_distance = curr_czas + czas + 0
                if new_distance < distances[rozklad][sasiad]:
                    distances[rozklad][sasiad] = new_distance
                    heapq.heappush(pq, (new_distance, sasiad, rozklad))
            if curr_rozklad + rozklad == 0:
                new_distance = curr_czas + czas + 10
                if new_distance < distances[rozklad][sasiad]:
                    distances[rozklad][sasiad] = new_distance
                    heapq.heappush(pq,(new_distance,sasiad,rozklad))
            if curr_rozklad + rozklad == 2:
                new_distance = curr_czas + czas + 5
                if new_distance < distances[rozklad][sasiad]:
                    distances[rozklad][sasiad] = new_distance
                    heapq.heappush(pq, (new_distance, sasiad, rozklad))
            if curr_rozklad + rozklad == 1:
                new_distance = curr_czas + czas + 20
                if new_distance < distances[rozklad][sasiad]:
                    distances[rozklad][sasiad] = new_distance
                    heapq.heappush(pq, (new_distance, sasiad, rozklad))
    return min(distances[0][B],distances[1][B])

def sol2_bucket(E,B,A):
    V_max = max(max(u,v) for u,v,czas,typ in E)
    adj_list = [[] for _ in range(V_max + 1)]
    for u,v,czass,typp in E:
        if typp == "P":
            adj_list[u].append((czass,v,0))
            adj_list[v].append((czass,u,0))
        else:
            adj_list[u].append((czass, v, 1))
            adj_list[v].append((czass, u, 1))
    distances = [[float("inf")] * (V_max+1) for _ in range(4)]
    distances[3][A] = 0
    buckets = [[] for _ in range(V_max * 30)]
    obecny_czas = 0
    buckets[obecny_czas].append((A,3))
    while obecny_czas < len(buckets):
        if not buckets[obecny_czas]:
            obecny_czas+=1
            continue
        curr_v,curr_rozklad = buckets[obecny_czas].pop()
        curr_czas = obecny_czas
        if curr_czas > distances[curr_rozklad][curr_v]:
            continue
        for czas,sasiad,rozklad in adj_list[curr_v]:
            if curr_rozklad == 3:
                new_distance = curr_czas + czas + 0
                if new_distance < distances[rozklad][sasiad]:
                    distances[rozklad][sasiad] = new_distance
                    buckets[new_distance].append((sasiad,rozklad))
            if curr_rozklad + rozklad == 0:
                new_distance = curr_czas + czas + 10
                if new_distance < distances[rozklad][sasiad]:
                    distances[rozklad][sasiad] = new_distance
                    buckets[new_distance].append((sasiad,rozklad))
            if curr_rozklad + rozklad == 2:
                new_distance = curr_czas + czas + 5
                if new_distance < distances[rozklad][sasiad]:
                    distances[rozklad][sasiad] = new_distance
                    buckets[new_distance].append((sasiad,rozklad))
            if curr_rozklad + rozklad == 1:
                new_distance = curr_czas + czas + 20
                if new_distance < distances[rozklad][sasiad]:
                    distances[rozklad][sasiad] = new_distance
                    buckets[new_distance].append((sasiad,rozklad))
    return min(distances[0][B],distances[1][B])
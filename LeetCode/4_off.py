import sys
import heapq
import math
sys.set_int_max_str_digits(0)
input_data = sys.stdin.read().split()
if not input_data:
    sys.exit(0)
data = iter(input_data)
n = int(next(data))
m = int(next(data))
k = int(next(data))
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    u = int(next(data))
    v = int(next(data))
    waga = int(next(data))
    adj_list[u].append((waga,v))
    adj_list[v].append((waga,u))
targets = []
for _ in range(k):
    targets.append(int(next(data)))
distances = [float("inf")] * (n+1)
distances[1] = 0
pq = [(0.0,1,1)]
schroniska = [0] * (n+1)
schroniska[1] = 1
rodzice = [(0,0)] * (n+1)
while pq:
    log_distance,liczba_schronisk,curr_node= heapq.heappop(pq)
    if log_distance > distances[curr_node]:
        continue
    for waga,sasiedzi in adj_list[curr_node]:
        nowy_log = log_distance + math.log(waga)
        if nowy_log < distances[sasiedzi]:
            distances[sasiedzi] = nowy_log
            schroniska[sasiedzi] = liczba_schronisk + 1
            rodzice[sasiedzi] = (curr_node,waga)
            heapq.heappush(pq,(nowy_log,liczba_schronisk+1,sasiedzi))
for i in range(len(targets)):
    curr = targets[i]
    sciezka = []
    ostateczny_czas = 1
    while curr != 1:
        sciezka.append(curr)
        poprzednik,waga_przejscia = rodzice[curr]
        ostateczny_czas *= waga_przejscia
        curr = poprzednik
    sciezka.append(1)
    sciezka.reverse()
    print(f"{schroniska[targets[i]]} {" ".join(map(str,sciezka))} {ostateczny_czas}")

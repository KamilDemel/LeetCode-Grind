import collections
import sys
wejscie = sys.stdin.read().split()
if not wejscie:
    sys.exit()
dane = iter(wejscie)
n = int(next(dane))
m = int(next(dane))
q = int(next(dane))
d = int(next(dane))
adj_list = [[] for _ in range(n + 1)]
wszystkie_wysokosci = set()
for _ in range(m):
    u = int(next(dane))
    v = int(next(dane))
    wysokosc_korytarza = int(next(dane))
    adj_list[u].append((wysokosc_korytarza, v))
    adj_list[v].append((wysokosc_korytarza, u))
    wszystkie_wysokosci.add(wysokosc_korytarza)
for i in range(1, n + 1):
    adj_list[i].sort()
posortowane_wysokosci = sorted(list(wszystkie_wysokosci))
zapytania = []
for _ in range(q):
    start = int(next(dane))
    cel = int(next(dane))
    zapytania.append((start, cel))
for start, cel in zapytania:
    czy_dasieprzejsc = False
    for dolna_granica in posortowane_wysokosci:
        gorna_granica = dolna_granica + d
        visited = [False] * (n + 1)
        kolejka = collections.deque()
        kolejka.append(start)
        visited[start] = True
        dotarl = False
        while kolejka:
            curr_node = kolejka.popleft()
            if curr_node == cel:
                dotarl = True
                break
            for wysokosc, sasiad in adj_list[curr_node]:
                if wysokosc > gorna_granica:
                    break
                if not visited[sasiad] and wysokosc >= dolna_granica:
                    visited[sasiad] = True
                    kolejka.append(sasiad)
        if dotarl:
            czy_dasieprzejsc = True
            break
    if czy_dasieprzejsc:
        print("TAK")
    else:
        print("NIE")
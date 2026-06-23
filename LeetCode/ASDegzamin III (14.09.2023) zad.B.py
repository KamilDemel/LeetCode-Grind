import heapq
def uncool(P):
    for i in range(len(P)):
        for j in range(len(P)):
            a,b = P[i]
            c,d = P[j]
            if a == c and b == d:
                continue
            if a < c and b > c and b < d:
                return (i,j)

def uncool_v2(P):
    przedzialy = [(P[i][0], P[i][1], i) for i in range(len(P))]
    przedzialy.sort(key=lambda x: (x[0], -x[1]))
    aktywne_konce = []
    for start, koniec, idx in przedzialy:
        while aktywne_konce and aktywne_konce[0][0] <= start:
            heapq.heappop(aktywne_konce)
        if aktywne_konce and aktywne_konce[0][0] < koniec:
            return (aktywne_konce[0][1], idx)
        heapq.heappush(aktywne_konce, (koniec, idx))
import heapq
def solution(points,k):
    odleglosci = [(-((points[i][0] - 0)**2 + (points[i][1] - 0)**2),
                   [points[i][0],points[i][1]]) for i in range(len(points))]
    heapq.heapify(odleglosci)
    while len(odleglosci) > k:
        heapq.heappop(odleglosci)
    wynik = []
    for distance,res in odleglosci:
        wynik.append(res)
    return wynik
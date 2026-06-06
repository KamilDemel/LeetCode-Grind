class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False
def sol(G):
    n = len(G)
    wagi = []
    for u in range(n):
        for v, waga in G[u]:
            if u < v:
                wagi.append((waga, u, v))
    wagi.sort()
    all_krawedzie = len(wagi)
    best_suma = float("inf")
    for i in range(all_krawedzie-n+2):
        suma = 0
        czy_bez_cykli = True
        uf = UnionFind(n)
        for j in range(n-1):
            krawedz = wagi[i+j]
            waga,u,v = krawedz
            if uf.union(u,v):
                suma += waga
            else:
                czy_bez_cykli = False
                break
        if suma < best_suma and czy_bez_cykli:
            best_suma = suma
    return best_suma




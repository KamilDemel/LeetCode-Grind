def sol(graph):
    wynik = []
    def dfs(node=0,sciezka=None):
        if not sciezka:
            sciezka = []
        if node == len(graph) - 1:
            wynik.append(sciezka + [node])
            return
        for sasiedzi in graph[node]:
            dfs(sasiedzi,sciezka+[node])
    dfs()
    return wynik
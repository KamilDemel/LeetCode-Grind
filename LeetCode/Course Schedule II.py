def solution(prereq,n):
    adj_list = [[] for _ in range(n)]
    for u,v in prereq:
        adj_list[u].append(v)
    stany = [0] * n
    wyniki = []
    def dfs(wezel):
        stany[wezel] = 1
        for sasiad in adj_list[wezel]:
            if stany[sasiad] == 1:
                return False
            elif stany[sasiad] == 0:
                if dfs(sasiad) == False:
                    return False
        stany[wezel] = 2
        wyniki.append(wezel)
        return True
    for i in range(len(adj_list)):
        if stany[i] == 0:
            if dfs(i) == False:
                return []
    return wyniki
def insertion_sort(T):
    n = len(T)
    if n <= 1:
        return
    for i in range(1,n):
        key = T[i]
        j = i - 1
        while j >= 0 and key < T[j]:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
def SortTab(T,P):
    N = len(T)
    tab_gestosci = []
    wynik_gestosc = [0] * N
    kubelki = [[] for _ in range(N)]
    for i in range(len(P)):
        tab_gestosci.append((P[i][0],P[i][1],P[i][2]/(P[i][1] - P[i][0])))
    for i in range(len(tab_gestosci)):
        wynik_gestosc[tab_gestosci[i][0] - 1] += tab_gestosci[i][2]
        wynik_gestosc[tab_gestosci[i][1] - 1] -= tab_gestosci[i][2]
    sum = 0
    for i in range(len(wynik_gestosc)):
        sum += wynik_gestosc[i]
        wynik_gestosc[i] = sum
    CDF = [0] * (N + 1)
    for i in range(N):
        CDF[i + 1] = CDF[i] + wynik_gestosc[i]
    for i in range(len(T)):
        calkowita = int(T[i])
        reszta = T[i] - calkowita
        P_total = CDF[calkowita - 1] + reszta * wynik_gestosc[calkowita - 1]
        kubelki[int(P_total * N)].append(T[i])
    res = []
    for i in range(len(kubelki)):
        if not kubelki[i]:
            continue
        if len(kubelki[i]) > 1:
            insertion_sort(kubelki[i])
            for j in range(len(kubelki[i])):
                res.append(kubelki[i][j])
        else:
            res.append(kubelki[i][0])
    return res



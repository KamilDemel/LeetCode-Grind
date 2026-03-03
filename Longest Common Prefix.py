def f(strs):
    dl_tab = len(strs)
    wynik = []
    for i in range(dl_tab):
        wynik.append(len(strs[i]))
    g = min(wynik)
    max_pre = ""
    for i in range(g):
        prev = strs[0][i]
        for j in range(1, dl_tab):
            new = strs[j][i]
            if prev != new:
                return max_pre
        max_pre += strs[0][i]
    return max_pre




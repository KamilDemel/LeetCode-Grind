def treecut(H,k):
    tab_par = [(H[i],i) for i in range(len(H))]
    inv_count = [0] * len(H)
    def merge(lewa,prawa):
        L = 0
        R = 0
        wynik = []
        while L < len(lewa) and R < len(prawa):
            if lewa[L][0] < prawa[R][0]:
                wynik.append((lewa[L][0],lewa[L][1]))
                L += 1
            else:
                wynik.append((prawa[R][0],prawa[R][1]))
                inv_count[prawa[R][1]] += len(lewa) - L
                R += 1
        while L < len(lewa):
            wynik.append((lewa[L][0],lewa[L][1]))
            L += 1
        while R < len(prawa):
            wynik.append((prawa[R][0],prawa[R][1]))
            R += 1
        return wynik
    def meerge_sort(T):
        if len(T) < 2:
            return T
        mid = len(T) // 2
        lewa_polowa = T[:mid]
        prawa_polowa = T[mid:]
        lewa_sorted = meerge_sort(lewa_polowa)
        prawa_sorted = meerge_sort(prawa_polowa)
        wynik = merge(lewa_sorted,prawa_sorted)
        return wynik
    meerge_sort(tab_par)
    suma_inwersji = 0
    for i in range(len(inv_count)):
        suma_inwersji += inv_count[i]
        if suma_inwersji > k:
            return i
    return len(H)


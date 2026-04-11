def pretty_sort(T):
    new_T = [str(T[i]) for i in range(len(T))]
    res = []
    for i in range(len(new_T)):
        tab_range = [0] * 10
        for j in range(len(new_T[i])):
            tab_range[int(new_T[i][j])] += 1
        res.append(tab_range)
    res_wynikowa = []
    for i in range(len(res)):
        ctr_jedynek = 0
        ctr_wielo = 0
        for j in range(len(res[i])):
            if res[i][j] == 1:
                ctr_jedynek += 1
            elif res[i][j] > 1:
                ctr_wielo += 1
        res_wynikowa.append((ctr_jedynek,ctr_wielo,T[i]))
    def merge(left,right):
        L = 0
        R = 0
        new_list = []
        while L < len(left) and R < len(right):
            if left[L][0] > right[R][0]:
                czy_L_lepszy = True
            elif left[L][0] == right[R][0] and left[L][1] < right[R][1]:
                czy_L_lepszy = True
            elif left[L][0] == right[R][0] and left[L][1] == right[R][1]:
                czy_L_lepszy = True
            else:
                czy_L_lepszy = False
            if czy_L_lepszy:
                new_list.append(left[L])
                L += 1
            else:
                new_list.append(right[R])
                R += 1
        while L < len(left):
            new_list.append(left[L])
            L += 1
        while R < len(right):
            new_list.append(right[R])
            R += 1
        return new_list
    def merge_sort(T):
        if len(T) < 2:
            return T
        mid = len(T) // 2
        left_tab = T[:mid]
        right_tab = T[mid:]
        sorted_left = merge_sort(left_tab)
        sorted_right = merge_sort(right_tab)
        return merge(sorted_left,sorted_right)
    wynik = merge_sort(res_wynikowa)
    return [wynik[i][2] for i in range(len(wynik))]


def pretty_sort_v2(T):
    new_T = [str(T[i]) for i in range(len(T))]
    res = []
    for i in range(len(new_T)):
        tab_range = [0] * 10
        for j in range(len(new_T[i])):
            tab_range[int(new_T[i][j])] += 1
        res.append(tab_range)
    macierz_kubelkow = [[[] for _ in range(11)] for _ in range(11)]
    for i in range(len(res)):
        ctr_jedynek = 0
        ctr_wielo = 0
        for j in range(len(res[i])):
            if res[i][j] == 1:
                ctr_jedynek += 1
            elif res[i][j] > 1:
                ctr_wielo += 1
        macierz_kubelkow[ctr_jedynek][ctr_wielo].append(T[i])
    wynik = []
    for j in range(10,-1,-1):
        for w in range(11):
            for liczba in macierz_kubelkow[j][w]:
                wynik.append(liczba)
    return wynik



def merge(left, right):
    R = 0
    L = 0
    new_list = []
    while L < len(left) and R < len(right):
        if left[L] < right[R]:
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
    if len(T) <= 1:
        return T
    mid = len(T) // 2
    left_tab = T[:mid]
    right_tab = T[mid:]
    sort_left = merge_sort(left_tab)
    sort_right = merge_sort(right_tab)
    return merge(sort_left,sort_right)
def ogrodzenie_v1(M,D,T):
    sorted_T = merge_sort(T)
    obecny = sorted_T[0]
    ctr = 0
    for i in range(1, len(sorted_T)):
        if sorted_T[i] - obecny >= D:
            ctr += 1
        obecny = sorted_T[i]
    return ctr
def ogrodzenie_v2(M,D,T):
    ilosc_kubelkow = int(M/D)+1
    kubelki = [[float("inf"),-1] for _ in range(ilosc_kubelkow)]
    for i in range(len(T)):
         kubelki[int(T[i] / D)][0] = min(kubelki[int(T[i] / D)][0],T[i])
         kubelki[int(T[i] / D)][1] = max(kubelki[int(T[i] / D)][1], T[i])
    akt_k = None
    ctr = 0
    for i in range(len(kubelki)):
        if kubelki[i][0] == float('inf') and kubelki[i][1] == -1:
            continue
        if not akt_k:
            akt_k = kubelki[i]
            continue
        if kubelki[i][0] - akt_k[1] >= D:
            ctr += 1
        akt_k = kubelki[i]
    return ctr
def bubble_sort(T):
    for i in range(len(T)):
        for j in range(i+1,len(T)):
            if T[j] < T[i]:
                T[i],T[j] = T[j],T[i]
    return T
def ogrodzenie_v3(M,D,T):
    n = len(T)
    ilosc_kubelkow = n
    kubelki = [[] for _ in range(ilosc_kubelkow)]
    for i in range(n):
        kubelki[min(int(T[i]/(M/n)),n - 1)].append(T[i])
    for i in range(len(kubelki)):
        if len(kubelki[i]) < 2:
            continue
        else:
            bubble_sort(kubelki[i])
    ctr = 0
    ostatni_palik = None
    for i in range(len(kubelki)):
        if not kubelki[i]: continue
        if len(kubelki[i]) > 1:
            prev = kubelki[i][0]
            for j in range(len(kubelki[i])):
                if kubelki[i][j] - prev >= D:
                    ctr += 1
                prev = kubelki[i][j]
        if i > 0 and kubelki[i] != [] and ostatni_palik:
            if kubelki[i][0] - ostatni_palik >= D:
                ctr += 1
        ostatni_palik = kubelki[i][-1]
    return ctr






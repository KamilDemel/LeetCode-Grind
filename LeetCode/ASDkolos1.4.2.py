def f(T):
    tab = []
    for i in range(len(T)):
        tab_alfa = ([0] * 26,i)
        for j in range(len(T[i])):
            tab_alfa[0][ord(T[i][j]) - ord("a")] += 1
        tab.append(tab_alfa)
    def merge(left,right):
        L = 0
        R = 0
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
        if len(T) < 2:
            return T
        mid = len(T) // 2
        lewy_tab = T[:mid]
        prawy_tab = T[mid:]
        sorted_left = merge_sort(lewy_tab)
        sorted_right = merge_sort(prawy_tab)
        return merge(sorted_left,sorted_right)
    res_krotka = merge_sort(tab)
    prev = res_krotka[0][0]
    ctr = 1
    max_ctr = 1
    for i in range(1,len(res_krotka)):
        if res_krotka[i][0] == prev:
            ctr += 1
            if ctr > max_ctr:
                max_ctr = ctr
        else:
            ctr = 1
        prev = res_krotka[i][0]
    return max_ctr

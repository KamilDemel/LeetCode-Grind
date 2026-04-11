def g(T):
    n = len(T)
    for i in range(n):
        org = T[i]
        pal = org[::-1]
        if org > pal:
            T[i] = pal
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
        lewa_tab = T[:mid]
        prawa_tab = T[mid:]
        sorted_left = merge_sort(lewa_tab)
        sorted_right = merge_sort(prawa_tab)
        return merge(sorted_left,sorted_right)
    sorted_T = merge_sort(T)
    prev = sorted_T[0]
    ctr = 1
    max_ctr = 1
    for i in range(1,len(T)):
        if sorted_T[i] == prev:
            ctr += 1
            if ctr > max_ctr:
                max_ctr = ctr
        else:
            ctr = 1
        prev = sorted_T[i]
    return max_ctr
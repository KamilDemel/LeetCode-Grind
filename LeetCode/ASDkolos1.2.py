def maxrank(T):
    max_rank = 0
    for i in range(1,len(T)):
        ctr = 0
        for j in range(i):
            if T[i] > T[j]:
                ctr += 1
        if ctr > max_rank:
            max_rank = ctr
    return max_rank
def maxrank_v2(T):
    wyniki = [0] * len(T)
    T_krotka = [(T[i], i) for i in range(len(T))]
    def merge(left, right):
        R = 0
        L = 0
        new_list = []
        l_count = 0
        while L < len(left) and R < len(right):
            if left[L][0] < right[R][0]:
                new_list.append(left[L])
                l_count += 1
                L += 1
            else:
                new_list.append(right[R])
                wyniki[right[R][1]] += l_count
                R += 1
        while L < len(left):
            new_list.append(left[L])
            L += 1
        while R < len(right):
            new_list.append(right[R])
            wyniki[right[R][1]] += l_count
            R += 1
        return new_list
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_tab = arr[:mid]
        right_tab = arr[mid:]
        sort_left = merge_sort(left_tab)
        sort_right = merge_sort(right_tab)
        return merge(sort_left,sort_right)

    merge_sort(T_krotka)
    return max(wyniki)





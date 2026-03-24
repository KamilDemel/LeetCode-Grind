def partition(T, left, right):
    mid = (left + right) // 2
    L = left
    R = right
    pivot = T[mid]
    while L <= R:
        while L <= right and T[L] < pivot:
            L += 1
        while R >= left and T[R] > pivot:
            R -= 1
        if L <= R:
            T[L],T[R]=T[R],T[L]
            L += 1
            R -= 1
    return L
def quick_sort(T,left,right):
    if left >= right:
        return T
    split_point = partition(T,left,right)
    quick_sort(T,left,split_point - 1)
    quick_sort(T,split_point,right)

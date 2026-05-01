def k_big(A,k):
    A_2D = []
    for i in range(len(A)):
        for j in range(len(A)):
            A_2D.append(A[i] * A[j])
    def partition(T,left,right):
        i = left
        pivot = T[right]
        for j in range(left,right):
            if T[j] > pivot:
                T[i],T[j] = T[j],T[i]
                i += 1
        T[right],T[i] = T[i],T[right]
        return i
    def quick_select(T,left,right,idx):
        i = partition(T,left,right)
        if i == idx:
            return T[i]
        elif idx < i:
            return quick_select(T,left,i-1,idx)
        else:
            return quick_select(T,i+1,right,idx)
    left = 0
    right = len(A_2D) - 1
    res = quick_select(A_2D,left,right,k - 1)
    return res
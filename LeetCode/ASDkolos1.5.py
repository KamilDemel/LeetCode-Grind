def Median(T):
    N = len(T)
    T_1D = [T[i][j] for i in range(N) for j in range(N)]
    def partition(T,left,right):
        pivot = T[right]
        i = left
        for j in range(left,right):
            if T[j] < pivot:
                T[j],T[i] = T[i],T[j]
                i += 1
        T[right],T[i] = T[i], T[right]
        return i
    def quick_select(T,left,right,idx):
        i = partition(T,left,right)
        if i == idx:
            return T[i]
        elif idx < i:
            return quick_select(T,left, i - 1, idx)
        else:
            return quick_select(T,i + 1, right, idx)
    all_elem = N * N
    polowa_z_reszty = (N**2 - N) // 2
    quick_select(T_1D, 0, N * N - 1, polowa_z_reszty)
    quick_select(T_1D,0,N * N - 1, polowa_z_reszty + N)
    pod = T_1D[0:polowa_z_reszty]
    na = T_1D[polowa_z_reszty:polowa_z_reszty+N]
    nad = T_1D[polowa_z_reszty+N:all_elem]
    ctr_pod = 0
    ctr_na = 0
    ctr_nad = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                T[i][j] = na[ctr_na]
                ctr_na += 1
            elif i > j:
                T[i][j] = pod[ctr_pod]
                ctr_pod += 1
            else:
                T[i][j] = nad[ctr_nad]
                ctr_nad += 1
    return T


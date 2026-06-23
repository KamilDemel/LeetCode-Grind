def coal(A,T):
    n = len(A)
    ostatni_idx = None
    magazyny = [T for _ in range(n)]
    for transport in A:
        for i in range(n):
            if magazyny[i] >= transport:
                magazyny[i] -= transport
                ostatni_idx = i
                break
    return ostatni_idx
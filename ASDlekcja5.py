def NWD(a,b):
    if b == 0:
        return a
    else:
        return NWD(b,a%b)
def move(T,k):
    N = len(T)
    nwd = NWD(N,k)
    for i in range(nwd):
        curr = (i+k) % N
        while curr != i:
            T[i],T[curr] = T[curr],T[i]
            curr+=k
            curr %= N
    return T
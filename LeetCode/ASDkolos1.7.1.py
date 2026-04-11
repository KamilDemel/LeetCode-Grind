def partition(T,left,right):
    i = left
    pivot = T[right]
    for j in range(left,right):
        if T[j] < pivot:
            T[i],T[j] = T[j],T[i]
            i += 1
    T[right],T[i]= T[i],T[right]
    return i
def quickselect(T,left,right,idx):
    i = partition(T,left,right)
    if idx == i:
        return T[i]
    elif idx < i:
        return quickselect(T,left,i-1,idx)
    else:
        return quickselect(T,i+1,right,idx)
def section(T,p,q):
    quickselect(T,0,len(T) - 1, p)
    quickselect(T,p,len(T)-1,q)
    wynik = sum(T[p:q+1])
    return wynik
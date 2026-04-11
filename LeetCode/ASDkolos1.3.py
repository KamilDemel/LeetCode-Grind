def partition(T,left,right):
    pivot = T[right]
    i = left
    for j in range(left,right):
        if T[j] < pivot:
            T[i],T[j] = T[j],T[i]
            i+=1
    T[right],T[i] = T[i],T[right]
    return i
def quick_select(T,left,right,idx):
    i = partition(T,left,right)
    if i == idx:
        return T[i]
    elif idx < i:
        return quick_select(T, left, i - 1, idx)
    else:
        return quick_select(T,i+1,right,idx)
def ksum(T,k,p):
    n = len(T)
    sum = 0
    for i in range(n-p+1):
        tab = T[i:i+p]
        sum += quick_select(tab,0,len(tab)-1,p-k)
    return sum

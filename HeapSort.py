def heapify(A,n,i):
    max = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and  A[max] < A[left]:
        max = left
    if right < n and A[max] < A[right]:
        max = right
    if max != i:
        A[i],A[max] = A[max],A[i]
        heapify(A,n,max)
def build_heap(A,n):
    for i in range(n//2 - 1, -1, -1):
        heapify(A,n,i)
def heap_sort(A):
    n = len(A)
    build_heap(A,n)
    for i in range(n - 1, -1, -1):
        A[0],A[i] = A[i],A[0]
        heapify(A,i,0)

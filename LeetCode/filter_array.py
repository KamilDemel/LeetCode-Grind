from collections import defaultdict
import math
def is_prime(nums):
    if nums < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(nums)) + 1):
            if nums % i == 0:
                return False
    return True
def solution(A,B):
    hash_map = defaultdict(int)
    n = len(A)
    k = len(B)
    for i in range(k):
        hash_map[B[i]] += 1
    for key,values in list(hash_map.items()):
        if not is_prime(values):
            del hash_map[key]
    C = []
    for j in range(n):
        if A[j] not in hash_map.keys():
            C.append(A[j])
    return C
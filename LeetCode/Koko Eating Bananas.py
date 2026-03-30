import math
def sol(piles,h):
    left = 1
    right = max(piles)
    n = len(piles)
    while left <= right:
        ile_h = 0
        mid = (left + right) // 2
        for i in range(n):
            ile_h += math.ceil(piles[i] / mid)
        if ile_h > h:
            left = mid + 1
        else:
            right = mid - 1
    return left





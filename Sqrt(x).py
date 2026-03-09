"""
def f(x):
    i = 2
    if x == 0:
        return 0
    if x < 4:
        return 1
    while True:
        if x >= (i * i) and x < (i+1) * (i+1):
            return i
        i+=1
"""
def f_bin(x):
    left = 0
    right = x
    if x == 1:
        return 1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid
        else:
            left = mid
        if right - left == 1:
            return left
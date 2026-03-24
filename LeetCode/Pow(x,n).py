"""
def f(x,n):
    res = 1
    if n == 0:
        return 1
    if x == 1.0:
        return 1.0
    if x == -1.0:
        return 1.0 if n % 2 == 0 else -1.0
    if n > 0:
        for _ in range(n):
            res *= x
    else:
        x = 1/x
        n = abs(n)
        for _ in range(n):
            res *= x
    return res
"""
def f(x,n):
    temp_n = abs(n)
    res = 1
    while temp_n > 0:
        if temp_n % 2 == 0:
            x = x * x
            temp_n = temp_n / 2
        else:
            res *= x
            temp_n -= 1
    return 1/res if n < 0 else res

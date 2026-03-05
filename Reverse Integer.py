def f(num_c):
    num = abs(num_c)
    len_n = 0
    temp = num
    while temp > 0:
        len_n+=1
        temp = temp // 10
    res = 0
    while num > 0:
        last = num % 10
        res = res + last * 10**(len_n-1)
        num = num // 10
        len_n -= 1
    if res < -2**31 or res > 2**31:
        return 0
    if num_c >= 0:
        return res
    else:
        return -1 * res
"""
def fg(num_c):
    num = abs(num_c)
    num = str(num)
    res = num[::-1]
    res = int(res)
    if res < -2 ** 31 or res > 2 ** 31:
        return 0
    if num_c >= 0:
        return res
    else:
        return -1 * res
"""

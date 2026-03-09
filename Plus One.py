def f(digits):
    n = len(digits)
    res = 0
    multi = 10**(n-1)
    for i in range(n):
        res = res + (multi * digits[i])
        multi = multi // 10
    res+=1
    wynik = []
    while res > 0:
        last = res % 10
        wynik.append(last)
        res = res // 10
    return wynik[::-1]
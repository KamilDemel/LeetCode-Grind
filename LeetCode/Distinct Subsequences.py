def sol(s,t):
    memo = {}
    n = len(s)
    m = len(t)
    def reku(i=0,j=0):
        if (i,j) in memo:
            return memo[(i,j)]
        if j == m:
            return 1
        if i == n:
            return 0
        wynik = 0
        if s[i] == t[j]:
            wynik_pasuje = reku(i+1,j+1) + reku(i+1,j)
            wynik += wynik_pasuje
        else:
            wynik_nie_pasuje = reku(i+1,j)
            wynik += wynik_nie_pasuje
        memo[(i,j)] = wynik
        return wynik
    return reku()



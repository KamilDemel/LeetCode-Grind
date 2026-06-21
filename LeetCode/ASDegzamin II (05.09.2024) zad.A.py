def wired(T):
    memo = {}
    def reku(i=0,j=len(T) - 1):
        if (i,j) in memo:
            return memo[(i,j)]
        if i > j:
            return 0
        if (j - i + 1) % 2 == 1:
            return float("inf")
        wynik = float("inf")
        for k in range(i+1,j+1,2):
            wynik = min(wynik,reku(i+1,k-1) + reku(k+1,j) + (1 + abs(T[i]-T[k])))
        memo[(i,j)] = wynik
        return wynik
    return reku()
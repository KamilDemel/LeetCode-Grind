def solve(S):
    S.sort(reverse=True)
    wynik = 0
    for i in range(len(S)):
        if S[i] - i < 0:
            break
        wynik = wynik + (S[i] - i)
    return wynik

def snow_dp(S):
    n = len(S)
    memo = {}
    def solve(L, R, dzien):
        if (L,R,dzien) in memo:
            return memo[(L,R,dzien)]
        if L > R or dzien >= n:
            return 0
        najlepszy_wynik = 0
        for k in range(L, R + 1):
            ile_zbierzemy = max(0, S[k] - dzien)
            wjazd_zachod = ile_zbierzemy + solve(k + 1, R, dzien + 1)
            wjazd_wschod = ile_zbierzemy + solve(L, k - 1, dzien + 1)
            najlepszy_wynik = max(najlepszy_wynik, wjazd_zachod, wjazd_wschod)
        memo[(L,R,dzien)] = najlepszy_wynik
        return najlepszy_wynik
    return solve(0, n - 1, 0)
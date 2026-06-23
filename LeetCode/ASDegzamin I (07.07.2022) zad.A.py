def solve(S):
    S.sort(reverse=True)
    wynik = 0
    for i in range(len(S)):
        if S[i] - i < 0:
            break
        wynik = wynik + (S[i] - i)
    return wynik

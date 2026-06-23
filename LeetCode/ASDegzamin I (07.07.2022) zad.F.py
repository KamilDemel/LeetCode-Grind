def maze(L):
    n = len(L)
    memo = {}
    def dfs(i, j, skad_przyszedlem):
        if i < 0 or i >= n or j < 0 or j >= n or L[i][j] == "#":
            return float('-inf')
        if i == n - 1 and j == n - 1:
            return 0
        if (i, j, skad_przyszedlem) in memo:
            return memo[(i, j, skad_przyszedlem)]
        ans_gora = float('-inf')
        ans_prawo = float('-inf')
        ans_dol = float('-inf')
        if skad_przyszedlem != "DOL":
            ans_dol = dfs(i + 1, j, "GORA") + 1
        if skad_przyszedlem != "GORA":
            ans_gora = dfs(i - 1, j, "DOL") + 1
        ans_prawo = dfs(i, j + 1, "LEWO") + 1
        best_wynik = max(ans_prawo, ans_gora, ans_dol)
        memo[(i, j, skad_przyszedlem)] = best_wynik
        return best_wynik
    wynik = dfs(0, 0, "LEWO")
    if wynik == float("-inf"):
        return -1
    return wynik





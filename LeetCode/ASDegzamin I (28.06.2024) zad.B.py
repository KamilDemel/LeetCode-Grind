def kstrong(T, k):
    n = len(T)
    dp = [[float('-inf')] * (k + 1) for _ in range(n)]
    dp[0][0] = T[0]
    najlepszy_max = T[0]
    for i in range(1, n):
        for j in range(k + 1):
            bierzemy = T[i]
            if dp[i - 1][j] != float('-inf'):
                bierzemy = max(bierzemy, dp[i - 1][j] + T[i])
            usuwamy = float('-inf')
            if j > 0 and dp[i - 1][j - 1] != float('-inf'):
                usuwamy = dp[i - 1][j - 1]
            dp[i][j] = max(bierzemy, usuwamy)
            if dp[i][j] > najlepszy_max:
                najlepszy_max = dp[i][j]
    return najlepszy_max
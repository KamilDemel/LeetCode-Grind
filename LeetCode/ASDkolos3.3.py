def orchard_2d(T, m):
    n = len(T)
    dp = [[float('inf')] * m for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        rem = T[i] % m
        for r in range(m):
            dp[i + 1][r] = min(dp[i + 1][r], dp[i][r])
            nowa_reszta = (r + rem) % m
            dp[i + 1][nowa_reszta] = min(dp[i + 1][nowa_reszta], dp[i][r] + 1)
    return dp[n][sum(T) % m]
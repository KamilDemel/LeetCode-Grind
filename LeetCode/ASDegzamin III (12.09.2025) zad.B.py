def kom(X,Z,W):
    N = len(X)
    dp = [[-1] * (W + 1) for _ in range(N + 1)]
    dp[0][W] = 0
    for i in range(1, N + 1):
        x_i = X[i - 1]
        z_i = Z[i - 1]
        for z in range(W + 1):
            if dp[i - 1][z] == -1:
                continue
            aktualne_zwyciestwo = dp[i - 1][z]
            dp[i][z] = max(dp[i][z],dp[i-1][z])
            if z - z_i >= 0:
                dp[i][z - z_i] = max(dp[i][z-z_i], dp[i-1][z] + x_i)
            if z + z_i <= W and aktualne_zwyciestwo - x_i >= 0:
                dp[i][z + z_i] = max(dp[i][z + z_i], dp[i-1][z] - x_i)
    return max(dp[N])

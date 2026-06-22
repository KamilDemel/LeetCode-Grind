def planets(D,C,T,E):
    n = len(D)
    dp = [[float("inf")] * (E+1) for _ in range(n)]
    dp[0][0] = 0
    for i in range(n):
        planeta, koszt = T[i]
        if planeta >= i:
            dp[planeta][0] = min(dp[planeta][0], dp[i][0] + koszt)
        for b in range(E+1):
            if b < E:
                dp[i][b+1] = min(dp[i][b+1],dp[i][b] + C[i])
            if i + 1 < n and b >= D[i+1] - D[i]:
                dp[i+1][b-(D[i+1] - D[i])] = min(dp[i+1][b-(D[i+1] - D[i])], dp[i][b])
    return min(dp[n-1])




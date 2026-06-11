def transactions(M, T):
    T_sorted = sorted(T, key=lambda x: x[1])
    n = len(T_sorted)
    if n == 0:
        return M
    dp = [0] * n
    for i in range(n):
        start_i, end_i, koszt_i, kwota_koncowa_i = T_sorted[i]
        profit_i = kwota_koncowa_i - koszt_i
        dp_prev = dp[i - 1] if i > 0 else M
        dp[i] = dp_prev
        best_prev_money = M
        for j in range(i - 1, -1, -1):
            if T_sorted[j][1] < start_i:
                best_prev_money = dp[j]
                break
        if best_prev_money >= koszt_i:
            dp[i] = max(dp[i], best_prev_money + profit_i)
    return dp[-1]
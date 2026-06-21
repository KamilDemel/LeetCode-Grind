def transactions(M,T_arr):
    N = len(T_arr)
    T_arr.sort(key=lambda item: item[1])
    time_last = T_arr[-1][1]
    dp = [0] * (time_last + 1)
    dp[0] = M
    k = 0
    for i in range(1, time_last + 1):
        dp[i] = dp[i - 1]
        while k < N and T_arr[k][1] == i:
            s_i, e_i, p_i, q_i = T_arr[k]
            if dp[s_i - 1] >= p_i:
                dp[i] = max(dp[i], dp[s_i - 1] + (q_i - p_i))
            k += 1
    return dp[time_last]
def sol(prices):
    n = len(prices)
    dp_hold = [0] * n
    dp_sold = [0] * n
    dp_rest = [0] * n
    dp_hold[0] = -prices[0]
    dp_sold[0] = float("-inf")
    dp_rest[0] = 0
    for i in range(1,n):
        dp_hold[i] = max(dp_hold[i-1],dp_rest[i-1] - prices[i])
        dp_sold[i] = dp_hold[i-1] + prices[i]
        dp_rest[i] = max(dp_rest[i-1],dp_sold[i-1])
    return max(dp_rest[-1],dp_hold[-1],dp_sold[-1])
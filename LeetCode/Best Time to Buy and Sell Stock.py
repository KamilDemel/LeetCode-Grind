def f(prices):
    left = 0
    n = len(prices)
    max_proft = 0
    for right in range(1,n):
        profit = prices[right] - prices[left]
        if left <= right and prices[right] < prices[left]:
            left = right
        if profit > 0:
            if profit > max_proft:
                max_proft = profit
    return max_proft



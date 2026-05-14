def sol(nums):
    n = len(nums)
    dp = [0] * n
    dp[n-1] = nums[n-1]
    dp[n-2] = max(nums[n-2],nums[n-1])
    if len(dp) == 1:
        return dp[0]
    if len(dp) == 2:
        return max(dp[0],dp[1])
    for i in range(n-3,-1,-1):
        dp[i] = max(nums[i] + dp[i+2],dp[i+1])
    return max(dp[0],dp[1])
print(sol([2,1,1,2]))
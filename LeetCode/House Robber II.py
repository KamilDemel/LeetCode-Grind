class Solution:
    def rob(self, nums):
        def dp(nums):
            n = len(nums)
            dp = [0] * n
            if len(dp) == 1:
                return nums[0]
            if len(dp) == 2:
                return max(nums[0],nums[1])
            dp[n-1] = nums[n-1]
            dp[n-2] = max(nums[n-2],nums[n-1])
            for i in range(n-3,-1,-1):
                dp[i] = max(nums[i] + dp[i+2],dp[i+1])
            return max(dp[0],dp[1])
        first_tab = nums[:-1]
        second_tab = nums[1:]
        if len(first_tab) == 0:
            return nums[0]
        return max(dp(first_tab),dp(second_tab))
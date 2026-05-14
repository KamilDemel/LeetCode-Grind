def f(n):
    if n == 1:
        return 1
    a = 1
    b = 2
    for _ in range(3,n+1):
        a,b = b,a+b
    return b
class Solution:
    def climbStairs(self, n):
        memo = {}
        def f_reku(k):
            if k in memo:
                return memo[k]
            if k == 1:
                return 1
            if k == 2:
                return 2
            memo[k] = f_reku(k - 1) + f_reku(k - 2)
            return memo[k]
        return f_reku(n)
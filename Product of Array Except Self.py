def f(nums):
    prefix = 1
    postfix = 1
    n = len(nums)
    res = [1 for _ in range(n)]
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    for j in range(n-1,-1,-1):
        res[j] = res[j] * postfix
        postfix = postfix * nums[j]
    return res



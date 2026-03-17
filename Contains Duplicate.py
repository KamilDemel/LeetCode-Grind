from collections import Counter
def f(nums):
    n = len(nums)
    zbior = set()
    for i in range(n):
        if nums[i] not in zbior:
            zbior.add(nums[i])
        else:
            return True
    return False
def f2(nums):
    res = Counter(nums)
    for i in res.values():
        if i > 1:
            return True
    return False
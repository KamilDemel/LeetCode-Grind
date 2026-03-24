"""
def f(nums):
    seen = set()
    n = len(nums)
    for i in range(n):
        if nums[i] not in seen:
            seen.add(nums[i])
    return len(seen), list(seen)
"""
def f(nums):
    n = len(nums)
    left = 1
    prev = nums[0]
    for right in range(1,n):
        if nums[right] == prev:
            continue
        else:
            nums[left] = nums[right]
            left += 1
        prev = nums[right]
    return left

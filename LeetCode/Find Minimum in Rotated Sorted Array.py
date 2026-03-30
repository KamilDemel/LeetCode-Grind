def sol(nums):
    first = nums[0]
    n = len(nums)
    for i in range(1,n):
        if nums[i] < first:
            return nums[i]
        first = nums[i]
    else:
        return nums[0]
def sol_v2(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]



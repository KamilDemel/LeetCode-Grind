class Solution:
    def removeElement(self, nums, val):
        left = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1
        return left
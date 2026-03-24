"""
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
"""
class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_dict:
                return num_dict[diff],i
            num_dict[nums[i]] = i
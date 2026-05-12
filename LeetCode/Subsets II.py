class Solution(object):
    def subsets(self, nums):
        wyniki = []
        nums.sort()
        def reku_pomoc(idx=0,tab=None):
            if not tab:
                tab = []
            wyniki.append(tab[:])
            for i in range(idx,len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                tab.append(nums[i])
                reku_pomoc(i + 1, tab)
                tab.pop()
        reku_pomoc()
        return wyniki
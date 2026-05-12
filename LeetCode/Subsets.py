class Solution(object):
    def subsets(self, nums):
        wyniki = []
        def reku_pomoc(idx=0,tab=None):
            if not tab:
                tab = []
            if idx == len(nums):
                wyniki.append(tab)
                return
            reku_pomoc(idx+1,tab + [nums[idx]])
            reku_pomoc(idx+1,tab)
        reku_pomoc()
        return wyniki
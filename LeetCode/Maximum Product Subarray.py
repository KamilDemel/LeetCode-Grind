class Solution(object):
    def maxProduct(self, nums):
        obecny_max = nums[0]
        obecny_min = nums[0]
        najlepszy_wynik = nums[0]
        for i in range(1, len(nums)):
            opcja1 = nums[i]
            opcja2 = obecny_max * nums[i]
            opcja3 = obecny_min * nums[i]
            obecny_max = max(opcja1, opcja2, opcja3)
            obecny_min = min(opcja1, opcja2, opcja3)
            if obecny_max > najlepszy_wynik:
                najlepszy_wynik = obecny_max
        return najlepszy_wynik



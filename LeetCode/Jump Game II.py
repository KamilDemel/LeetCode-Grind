class Solution(object):
    def jump(self, nums):
        licznik_skokow = 0
        koniec_obecnego_skoku = 0
        najdalszy_zasieg = 0
        for i in range(len(nums) - 1):
            najdalszy_zasieg = max(najdalszy_zasieg, i + nums[i])
            if i == koniec_obecnego_skoku:
                licznik_skokow += 1
                koniec_obecnego_skoku = najdalszy_zasieg
        return licznik_skokow
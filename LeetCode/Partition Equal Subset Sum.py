class Solution(object):
    def canPartition(self, nums):
        suma_calkowita = sum(nums)
        if suma_calkowita % 2 != 0:
            return False
        cel = suma_calkowita // 2
        dp = {0}
        for num in nums:
            nowe_sumy = set()
            for dotychczasowa_suma in dp:
                nowa_suma = dotychczasowa_suma + num
                if nowa_suma == cel:
                    return True
                if nowa_suma < cel:
                    nowe_sumy.add(nowa_suma)
            dp.update(nowe_sumy)
        return False

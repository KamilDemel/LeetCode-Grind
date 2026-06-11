def sol(nums,target):
    memo = {}
    def reku_pomoc(idx=0,akt_suma=0):
        if (idx,akt_suma) in memo:
            return memo[(idx,akt_suma)]
        if idx == len(nums):
            if akt_suma == target:
                return 1
            return 0
        plus = reku_pomoc(idx+1,akt_suma+nums[idx])
        minus = reku_pomoc(idx+1,akt_suma-nums[idx])
        wynik = plus + minus
        memo[(idx,akt_suma)] = wynik
        return wynik
    return reku_pomoc()

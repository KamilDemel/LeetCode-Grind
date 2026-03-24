import math
class Solution:
    def countPrimes(self, n: int) -> int:
        T = [False, True] * ((n + 1) // 2)
        k = len(T)
        if k == 1:
            return 0
        T[0] = False
        T[1] = False
        for i in range(3, int(math.sqrt(n)) + 1,2):
            if T[i]:
                for j in range(i*i, k, i * 2):
                    T[j] = False
        T[2] = True
        ctr = 0
        for i in range(n):
            if T[i]:
                ctr+=1
        return ctr
my_sol = Solution()
wynik = my_sol.countPrimes(10)
print(wynik)

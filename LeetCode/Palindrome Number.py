import math
class Solution(object):
    def isPalindrome(self, x):
        """
        start = 0
        x = str(x)
        stop = len(x) - 1
        while start < stop:
            if x[start] != x[stop]:
                return False
            start+=1
            stop-=1
        return True
        """

        """
        x = str(x)
        return x == x[::-1]
        """

        if x < 0:
            return False
        if x == 0:
            return True
        mnoznik = 10
        dl = int(math.log10(x))
        while dl > 0:
            ostatnia_cyfra = x % mnoznik
            pierwsza_cyfra = x // (mnoznik**dl)
            if ostatnia_cyfra != pierwsza_cyfra:
                return False
            x = x % (mnoznik**dl) // 10
            dl -= 2
        return True
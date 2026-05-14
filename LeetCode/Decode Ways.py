class Solution(object):
    def numDecodings(self, s):
        memo = {}
        def reku_pomoc(idx=0):
            if idx in memo:
                return memo[idx]
            if idx == len(s):
                return 1
            if s[idx] == "0":
                return 0
            wynik = reku_pomoc(idx+1)
            if idx + 2 <= len(s) and int(s[idx:idx+2]) <= 26:
                wynik += reku_pomoc(idx+2)
            memo[idx] = wynik
            return wynik
        return reku_pomoc()


class Solution(object):
    def generateParenthesis(self, n):
        wynik = []
        def reku_pomoc(res="",ctr_otwarte=0,ctr_zamkniete=0):
            if len(res) == 2 * n:
                wynik.append(res)
                return
            if ctr_otwarte < n:
                reku_pomoc(res+"(",ctr_otwarte+1,ctr_zamkniete)
            if ctr_zamkniete < n and ctr_otwarte > ctr_zamkniete:
                reku_pomoc(res+")",ctr_otwarte,ctr_zamkniete+1)
        reku_pomoc()
        return wynik

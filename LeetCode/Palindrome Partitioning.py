class Solution(object):
    def partition(self, s):
        def czy_pal(tekst):
            return tekst == tekst[::-1]
        wynik = []
        def reku_pomoc(idx=0,sciezka=None):
            if not sciezka:
                sciezka = []
            if idx == len(s):
                wynik.append(sciezka[:])
                return
            for i in range(idx,len(s)):
                if czy_pal(s[idx:i+1]):
                    sciezka.append(s[idx:i+1])
                    reku_pomoc(i+1,sciezka)
                    sciezka.pop()
        reku_pomoc()
        return wynik
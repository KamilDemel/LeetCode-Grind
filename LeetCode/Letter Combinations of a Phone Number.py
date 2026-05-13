class Solution(object):
    def letterCombinations(self, digits):
        wynik = []
        slownik = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        possiblie_letters = []
        for num in digits:
            possiblie_letters.append(slownik[int(num)])
        def reku_pomoc(idx=0,sciezka=""):
            if idx == len(digits):
                wynik.append(sciezka)
                return
            for letter in possiblie_letters[idx]:
                reku_pomoc(idx + 1,sciezka+letter)
        reku_pomoc()
        return wynik
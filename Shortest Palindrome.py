class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        def if_pal(s):
            return s == s[::-1]
        def add_element(word, k):
            word = list(word)
            word.insert(0,k)
            return "".join(word)
        napis = ""
        temp = s
        while if_pal(temp) != True:
            last = temp[-1]
            napis += last
            temp = temp[:-1]
        res = add_element(s,napis)
        return res
        """
        if not s:
            return s
        combined = s + "#" + s[::-1]
        n = len(combined)
        lps = [0] * n
        for i in range(1, n):
            length = lps[i - 1]
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]
            if combined[i] == combined[length]:
                length += 1
            lps[i] = length
        longest_pal_prefix_len = lps[-1]
        non_pal_suffix = s[longest_pal_prefix_len:]
        return non_pal_suffix[::-1] + s
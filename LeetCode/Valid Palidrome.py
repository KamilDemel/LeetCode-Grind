class Solution:
    def isPalindrome(self, n_napis: str) -> bool:
        """
        napis = ""
        if s == " ":
            return True
        for i in s:
            if i.isalnum():
                napis+=i
        n_napis = napis.lower()
        return n_napis == n_napis[::-1]
        """
        n = len(n_napis)
        left = 0
        right = n - 1
        while left <= right:
            if not n_napis[left].isalnum():
                left += 1
                continue
            if not n_napis[right].isalnum():
                right -= 1
                continue
            if n_napis[left].lower() != n_napis[right].lower():
                return False
            left+=1
            right-=1
        return True
class Solution(object):
    def countSubstrings(self, s):
        dl = len(s)
        ctr = 0
        for i in range(dl):
            left_np = i
            right_np = i
            while left_np >= 0 and right_np < dl and s[left_np] == s[right_np]:
                left_np-=1
                right_np+=1
                ctr += 1
            left_p = i
            right_p = i + 1
            while left_p >= 0 and right_p < dl and s[left_p] == s[right_p]:
                left_p-=1
                right_p+=1
                ctr += 1
        return ctr
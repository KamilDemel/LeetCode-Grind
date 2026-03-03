"""
def longestPalindrome(s):
    dl = len(s)
    maxx = 0
    maxx_napis = ""
    for i in range(dl):
        for j in range(i+1,dl+1):
            podciag = s[i:j]
            dl_p = len(podciag)
            if podciag == podciag[::-1]:
                if dl_p > maxx:
                    maxx = dl_p
                    maxx_napis = podciag
    return maxx_napis
"""

def pal(s):
    dl = len(s)
    max_licznik = 0
    lewy_max = 0
    prawy_max = 0
    for i in range(dl):
        left_np = i
        right_np = i
        while left_np >= 0 and right_np < dl and s[left_np] == s[right_np]:
            left_np-=1
            right_np+=1
        dl_np = right_np - left_np - 1
        if dl_np > max_licznik:
            max_licznik = dl_np
            lewy_max = left_np
            prawy_max = right_np
        left_p = i
        right_p = i + 1
        while left_p >= 0 and right_p < dl and s[left_p] == s[right_p]:
            left_p-=1
            right_p+=1
        dl_p = right_p - left_p - 1
        if dl_p > max_licznik:
            max_licznik = dl_p
            lewy_max = left_p
            prawy_max = right_p
    return s[lewy_max+1:prawy_max]
from collections import defaultdict
def f(s1,s2):
    left = 0
    m = len(s1)
    n = len(s2)
    d_s1 = defaultdict(int)
    d_s2 = defaultdict(int)
    for i in range(m):
        elem = s1[i]
        d_s1[elem] += 1
    for right in range(n):
        d_s2[s2[right]] += 1
        window_len = right - left + 1
        if window_len > m:
            d_s2[s2[left]] -= 1
            if d_s2[s2[left]] == 0:
                del d_s2[s2[left]]
            left += 1
        if d_s1 == d_s2:
            return True
    return False

from collections import defaultdict
def f(s,k):
    left = 0
    n = len(s)
    d = defaultdict(int)
    first = s[left]
    d[first] += 1
    max_w = 1
    for right in range(1,n):
        elem = s[right]
        d[elem] += 1
        window_len = right - left + 1
        m = max(d.values())
        if window_len - m > k:
            d[s[left]] -= 1
            left += 1
        if right - left + 1 > max_w:
            max_w = right - left + 1
    return max_w

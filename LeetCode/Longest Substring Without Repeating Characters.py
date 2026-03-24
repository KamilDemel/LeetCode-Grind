"""
def f(word):
    n = len(word)
    max_ctr = 1
    if word == "":
        return 0
    for i in range(n):
        tab = set(word[i])
        ctr = 1
        for j in range(i+1,n):
            if word[j] not in tab:
                ctr += 1
                tab.add(word[j])
            else:
                break
        if ctr > max_ctr:
            max_ctr = ctr
    return max_ctr
"""

def swf(word):
    n = len(word)
    best_len = 0
    tab = set()
    left = 0
    for right in range(n):
        while word[right] in tab:
            tab.remove(word[left])
            left += 1
        tab.add(word[right])
        if len(tab) > best_len:
            best_len = len(tab)
    return best_len
from collections import Counter
import string
"""
def f(s):
    n = len(s)
    mid = n // 2
    word = s[:mid]
    word = "".join(sorted(word))
    if n % 2 == 0:
        return word + word[::-1]
    else:
        return word + s[mid] + word[::-1]
"""
def f_optimized(s):
    n = len(s)
    mid = n // 2
    word = s[:mid]
    ctr = Counter(word)
    napis = ""
    for char in string.ascii_lowercase:
        if char in ctr:
            ile = ctr[char]
            napis += ile * char
    if n % 2 == 0:
        return napis + napis[::-1]
    else:
        return napis + s[mid] + napis[::-1]

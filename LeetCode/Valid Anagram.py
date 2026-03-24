from collections import Counter
def is_anagramv1(s,t):
    if len(s) != len(t):
        return False
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t
def is_anagramv2(s,t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
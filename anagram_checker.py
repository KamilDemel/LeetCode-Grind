def count_sort(slowo):
    alfabet = [0] * 26
    a = ord("a")
    for i in range(len(slowo)):
        val = ord(slowo[i]) - a
        alfabet[val] += 1
    return alfabet
def if_anagram(a,b):
    if len(a) != len(b):
        return False
    x = count_sort(a)
    y = count_sort(b)
    for i in range(26):
        if x[i] != y[i]:
            return False
    return True

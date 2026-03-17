from collections import Counter
def f(nums,k):
    res = Counter(nums)
    keys = []
    wynik = res.most_common(k)
    for i in range(k):
        keys.append(wynik[i][0])
    return keys
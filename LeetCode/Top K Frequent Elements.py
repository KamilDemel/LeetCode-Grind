from collections import Counter
def f(nums,k):
    res = Counter(nums)
    keys = []
    wynik = res.most_common(k)
    for i in range(k):
        keys.append(wynik[i][0])
    return keys
def f_otpimized(nums,k):
    n = len(nums)
    res = Counter(nums)
    T = [[] for _ in range(n + 1)]
    for key,value in res.items():
        T[value].append(key)
    out_Res = []
    temp = k
    for j in range(len(T)-1,-1,-1):
        if temp > 0 and T[j] != []:
            out_Res.extend(T[j])
            temp -= len(T[j])
    return out_Res[:k]
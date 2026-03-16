def f(haystack,needle):
    n = len(haystack)
    k = len(needle)
    for i in range(n-k+1):
        if haystack[i] == needle[0]:
            for j in range(1,k):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
    return -1

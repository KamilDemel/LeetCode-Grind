def solution(edges):
    szefowie = [i for i in range(len(edges) + 1)]
    def findd(wezel):
        while wezel != szefowie[wezel]:
            wezel = szefowie[wezel]
        return wezel
    for p,q in edges:
        szef_p = findd(p)
        szef_q = findd(q)
        if szef_p == szef_q:
            return [p,q]
        szefowie[szef_q] = szef_p
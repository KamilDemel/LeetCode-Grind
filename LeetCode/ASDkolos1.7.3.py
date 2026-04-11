def solution(T2):
    t_krotki = [(len(T2[i]),T2[i]) for i in range(len(T2))]
    max_len = t_krotki[0][0]
    for i in range(1,len(t_krotki)):
        if t_krotki[i][0] > max_len:
            max_len = t_krotki[i][0]
    kubelki = [[] for _ in range(max_len + 1)]
    for i in range(len(T2)):
        kubelki[len(T2[i])].append(T2[i])
    res = []
    for i in range(len(kubelki)):
        if not kubelki[i]:
            continue
        res = res + kubelki[i]
    kubelki_liter = [[] for _ in range(26)]
    for i in range(max_len - 1, -1, -1):
        krotkie = []
        for j in range(len(res)):
            if len(res[j]) <= i:
                krotkie.append(res[j])
            else:
                kubelki_liter[ord(res[j][i]) - ord("a")].append(res[j])
        res = krotkie
        for kub in kubelki_liter:
            res = res + kub
        kubelki_liter = [[] for _ in range(26)]
    return res
def f(slowo):
    k = 3
    all_podciagi = []
    for i in range(len(slowo)-k+1):
        podciag = slowo[i:i+k]
        all_podciagi.append(podciag)
    kubelki = [[] for _ in range(2)]
    for j in range(k - 1, -1, -1):
        for i in range(len(all_podciagi)):
            if all_podciagi[i][j] == "a":
                kubelki[0].append(all_podciagi[i])
            else:
                kubelki[1].append(all_podciagi[i])
        all_podciagi = kubelki[0] + kubelki[1]
        kubelki = [[] for _ in range(2)]
    prev = all_podciagi[0]
    ctr = 1
    max_ctr = 1
    best_slowo = all_podciagi[0]
    for i in range(1,len(all_podciagi)):
        if all_podciagi[i] == prev:
            ctr += 1
            if ctr > max_ctr:
                max_ctr = ctr
                best_slowo = all_podciagi[i]
        else:
            ctr = 1
        prev = all_podciagi[i]
    return best_slowo
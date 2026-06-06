def parkiet(B, C, s):
    for wiersz in C:
        wiersz.append(0)
    C.append([0] * len(C[0]))
    i = 0
    j = 0
    ctr = 0
    while i < len(B) and j < len(B[0]):
        if C[i][j] <= s:
            return ctr
        seki_naj_wiersz = C[i][j] - C[i + 1][j]
        seki_naj_lewa_kolumna = C[i][j] - C[i][j + 1]
        if seki_naj_wiersz <= s:
            i += 1
            ctr += 1
        elif seki_naj_lewa_kolumna <= s:
            j += 1
            ctr += 1
        else:
            return -1
    return ctr
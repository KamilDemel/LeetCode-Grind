def sol(s):
    ostatnie_idx = {}
    for i in range(len(s)):
        ostatnie_idx[s[i]] = i
    end = 0
    wynik = []
    dl = 1
    for i in range(len(s)):
        end = max(ostatnie_idx[s[i]],end)
        if i == end:
            wynik.append(dl)
            dl = 0
        dl += 1
    return wynik
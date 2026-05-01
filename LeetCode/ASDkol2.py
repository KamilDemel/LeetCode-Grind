import collections
def change(mosty, poczty, s):
    mosty2 = []
    for u, v, nakrycie in mosty:
        if nakrycie == "F":
            mosty2.append((u, v, 0))
        else:
            mosty2.append((u, v, 1))
    V = max(max(u, w) for u, w, nakrycie in mosty2)
    adj_list = [[] for _ in range(V + 1)]
    for u, w, nakrycie in mosty2:
        adj_list[u].append((nakrycie, w))
        adj_list[w].append((nakrycie, u))
    start_point = s
    poczty = set(poczty)
    if start_point in poczty:
        return 0
    kolejka = collections.deque([(-1,start_point, -1)])
    distances = [[float('inf')] * 3 for _ in range(V + 1)]
    distances[start_point][0] = -1
    while kolejka:
        ilosc_zmian_czapek, curr_node, curr_czapka = kolejka.popleft()
        if curr_node in poczty:
            return ilosc_zmian_czapek
        if ilosc_zmian_czapek > distances[curr_node][curr_czapka+1]:
            continue
        for czapka, sasiad in adj_list[curr_node]:
            if curr_czapka != czapka:
                new_czapka = czapka
                nowa_ilosc = ilosc_zmian_czapek + 1
                idx_czapki = new_czapka + 1
                if nowa_ilosc < distances[sasiad][idx_czapki]:
                    distances[sasiad][idx_czapki] = nowa_ilosc
                    kolejka.append((nowa_ilosc, sasiad, czapka))
            else:
                nowa_ilosc = ilosc_zmian_czapek
                idx_czapki = czapka + 1
                if nowa_ilosc < distances[sasiad][idx_czapki]:
                    distances[sasiad][idx_czapki] = nowa_ilosc
                    kolejka.appendleft((nowa_ilosc, sasiad, czapka))
    return -1

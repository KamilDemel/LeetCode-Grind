from collections import Counter
def sol(hand, groupSize):
    hand.sort()
    idx = 0
    used_idx = set()
    while True:
        if idx in used_idx:
            idx += 1
            continue
        if len(used_idx) == len(hand):
            return True
        if idx == len(hand):
            return False
        used_idx.add(idx)
        ctr = 1
        for i in range(idx+1,len(hand)):
            if hand[i] - hand[idx] == ctr and i not in used_idx:
                used_idx.add(i)
                ctr += 1
                if groupSize == ctr:
                    break
        if ctr < groupSize:
            return False
        idx += 1
    return False
def sol2(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False
    wynik = Counter(hand)
    sorted_wynik = dict(sorted(wynik.items()))
    for wartosc in sorted_wynik.keys():
        ile = sorted_wynik[wartosc]
        if ile == 0:
            continue
        for i in range(groupSize):
            if wartosc + i in sorted_wynik and sorted_wynik[wartosc + i] >= ile:
                sorted_wynik[wartosc + i] -= ile
            else:
                return False
    return True






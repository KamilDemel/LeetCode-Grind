def kawa(T, k):
    notes = [0] * (k + 1)
    kasa = 0
    for x in reversed(T):
        for kwiaty in range(1, x):
            kasa += notes[kwiaty]
        notes[x] += 1
    return kasa


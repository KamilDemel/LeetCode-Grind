def sol(n):
    bin_n = bin(n)[2:]
    ctr = 0
    for cyfra in bin_n:
        if cyfra == "1":
            ctr += 1
    return ctr
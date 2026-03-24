def f(a,b):
    res_a = 0
    ctra = 0
    ctrb = 0
    res_b = 0
    for i in range(len(a) - 1,-1,-1):
        if a[i] == "1":
            res_a += 2**ctra
        ctra+=1
    for j in range(len(b) - 1, -1, -1):
        if b[j] == "1":
            res_b += 2**ctrb
        ctrb += 1
    total_sum = res_b + res_a
    return bin(total_sum)[2:]


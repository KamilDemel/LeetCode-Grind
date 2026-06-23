def magic(C):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    for i in range(n):
        if dp[i] == -1:
            continue
        for j in range(1,4):
            G = C[i][0]
            K,W = C[i][j]
            if W == -1:
                continue
            zysk = min(G-K,10)
            kasa_po_przejsciu = dp[i] + zysk
            if kasa_po_przejsciu >= 0:
                dp[W] = max(dp[W],kasa_po_przejsciu)
    return dp[n-1]



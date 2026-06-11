def reku(text1,text2):
    n = len(text1)
    m = len(text2)
    memo = {}
    def lcs(i=0,j=0):
        if (i,j) in memo:
            return memo[(i,j)]
        if i == n or j == m:
            return 0
        elif text1[i] == text2[j]:
            wynik =  1 + lcs(i+1,j+1)
        else:
            wynik =  max(lcs(i+1,j), lcs(i,j+1))
        memo[(i,j)] = wynik
        return wynik
    return lcs()
def sol(text1,text2):
    n = len(text1)
    m = len(text2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]
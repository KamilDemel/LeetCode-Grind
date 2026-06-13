def sol(s1,s2,s3):
    if len(s1) + len(s2) != len(s3):
        return False
    memo = {}
    def reku_pomoc(i=0,j=0):
        if (i,j) in memo:
            return memo[(i,j)]
        if i == len(s1) and j == len(s2):
            return True
        ans = False
        if i < len(s1) and s3[i+j] == s1[i]:
            ans = ans or reku_pomoc(i+1,j)
        if j < len(s2) and s3[i+j] == s2[j]:
            ans = ans or reku_pomoc(i,j+1)
        memo[(i,j)] = ans
        return ans
    return reku_pomoc()




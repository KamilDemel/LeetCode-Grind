def sol(s):
    memo = {}
    def reku(i=0,open_count=0):
        if (i,open_count) in memo:
            return memo[(i,open_count)]
        if open_count < 0:
            return False
        if i == len(s):
            if open_count == 0:
                return True
            return False
        ans = False
        if s[i] == "(":
            ans = ans or reku(i+1,open_count+1)
        if s[i] == ")":
            ans = ans or reku(i+1,open_count-1)
        if s[i] == "*":
            ans = ans or (reku(i+1,open_count) or reku(i+1,open_count+1) or reku(i+1,open_count-1))
        memo[(i,open_count)] = ans
        return ans
    return reku()




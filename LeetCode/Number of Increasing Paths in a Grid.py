def countPaths(grid):
    n = len(grid)
    m = len(grid[0])
    memo = {}
    def dfs(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        paths = 1
        if i + 1 < n and grid[i + 1][j] > grid[i][j]:
            paths += dfs(i+1,j)
        if j + 1 < m and grid[i][j + 1] > grid[i][j]:
            paths += dfs(i,j+1)
        if i - 1 >= 0 and grid[i - 1][j] > grid[i][j]:
            paths += dfs(i-1,j)
        if j - 1 >= 0 and grid[i][j - 1] > grid[i][j]:
            paths += dfs(i,j-1)
        memo[(i,j)] = paths
        return paths
    wynik = 0
    for i in range(n):
        for j in range(m):
            wynik += dfs(i,j)
    return wynik % (10**9 + 7)

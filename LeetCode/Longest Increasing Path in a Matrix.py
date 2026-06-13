import collections
def sol_bfs(matrix):
    n = len(matrix)
    m = len(matrix[0])
    best_ctr = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            element = matrix[i][j]
            kolejka = collections.deque()
            kolejka.append((element,i,j))
            ctr = 0
            while kolejka:
                ctr += 1
                for _ in range(len(kolejka)):
                    curr_liczba, curr_i, curr_j = kolejka.popleft()
                    if curr_i + 1 < n and matrix[curr_i+1][curr_j] > curr_liczba and (curr_i+1,curr_j):
                        kolejka.append((matrix[curr_i+1][curr_j],curr_i+1,curr_j))
                    if curr_j + 1 < m and matrix[curr_i][curr_j+1] > curr_liczba and (curr_i,curr_j+1):
                        kolejka.append((matrix[curr_i][curr_j+1],curr_i,curr_j+1))
                    if curr_i - 1 >= 0 and matrix[curr_i-1][curr_j] > curr_liczba and (curr_i-1,curr_j):
                        kolejka.append((matrix[curr_i-1][curr_j],curr_i-1,curr_j))
                    if curr_j - 1 >= 0 and matrix[curr_i][curr_j-1] > curr_liczba and (curr_i,curr_j-1):
                        kolejka.append((matrix[curr_i][curr_j-1],curr_i,curr_j-1))
            if ctr > best_ctr:
                best_ctr = ctr
    return best_ctr
def sol_dfs_memo(matrix):
    n = len(matrix)
    m = len(matrix[0])
    memo = {}
    def dfs(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        best_path = 1
        if i + 1 < n and matrix[i+1][j] > matrix[i][j]:
            best_path = max(best_path, 1 + dfs(i+1,j))
        if j + 1 < m and matrix[i][j+1] > matrix[i][j]:
            best_path = max(best_path, 1 + dfs(i,j+1))
        if i - 1 >= 0 and matrix[i-1][j] > matrix[i][j]:
            best_path = max(best_path, 1 + dfs(i-1,j))
        if j - 1 >= 0 and matrix[i][j-1] > matrix[i][j]:
            best_path = max(best_path, 1 + dfs(i,j-1))
        memo[(i,j)] = best_path
        return best_path
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans,dfs(i,j))
    return ans




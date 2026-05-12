class Solution(object):
    def exist(self, board, word):
        def dfs(i,j,idx_w):
            if idx_w == len(word):
                return True
            if 0 > i or i >= len(board) or 0 > j or j >= len(board[0]) or board[i][j] != word[idx_w]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            znaleziono = (dfs(i+1,j,idx_w+1) or dfs(i,j+1,idx_w+1) or dfs(i,j-1,idx_w+1) or dfs(i-1,j,idx_w+1))
            board[i][j] = temp
            return znaleziono
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
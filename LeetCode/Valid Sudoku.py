class Solution:
    def isValidSudoku(self, board):
        def check_rows(board):
            n = len(board)
            for i in range(n):
                res = set()
                for j in range(n):
                    if board[i][j] != ".":
                        if board[i][j] in res:
                            return False
                        else:
                            res.add(board[i][j])
            return True
        def check_columns(board):
            n = len(board)
            for i in range(n):
                res = set()
                for j in range(n):
                    if board[j][i] != ".":
                        if board[j][i] in res:
                            return False
                        else:
                            res.add(board[j][i])
            return True
        def valid3x3(board):
            n = len(board)
            for i in range(0,n-2,3):
                for j in range(0,n-2,3):
                    wyst = set()
                    for c in range(3):
                        for r in range(3):
                            if board[i+c][j+r] != ".":
                                if board[i+c][j+r] in wyst:
                                    return False
                                else:
                                    wyst.add(board[i+c][j+r])
            return True

        if check_rows(board) and check_columns(board) and valid3x3(board):
            return True
        else:
            return False


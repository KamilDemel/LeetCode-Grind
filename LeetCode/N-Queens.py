class Solution(object):
    def solveNQueens(self, n):
        col = set()
        pos_diag = set()
        neg_diag = set()
        res = []
        board = [["."] * n for _ in range(n)]
        def back_track(row=0):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for i in range(n):
                if i not in col and (row-i) not in neg_diag and (row+i) not in pos_diag:
                    col.add(i)
                    pos_diag.add(row+i)
                    neg_diag.add(row-i)
                    board[row][i] = "Q"
                    back_track(row+1)
                    col.remove(i)
                    pos_diag.remove(row+i)
                    neg_diag.remove(row-i)
                    board[row][i] = "."
        back_track()
        return res
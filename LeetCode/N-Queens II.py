class Solution(object):
    def totalNQueens(self, n):
        col = set()
        pos_diag = set()
        neg_diag = set()
        ctr = 0
        def back_track(row=0):
            nonlocal ctr
            if row == n:
                ctr += 1
                return
            for i in range(n):
                if i not in col and (row-i) not in neg_diag and (row+i) not in pos_diag:
                    col.add(i)
                    pos_diag.add(row+i)
                    neg_diag.add(row-i)
                    back_track(row+1)
                    col.remove(i)
                    pos_diag.remove(row+i)
                    neg_diag.remove(row-i)
        back_track()
        return ctr
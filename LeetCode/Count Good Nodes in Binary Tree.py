class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root):
        def dfs(node,max_so_far):
            if not node:
                return 0
            if node.val >= max_so_far:
                moj_wynik = 1
            else:
                moj_wynik = 0
            new_rekord = max(max_so_far,node.val)
            left = dfs(node.left,new_rekord)
            right = dfs(node.right,new_rekord)
            return moj_wynik + left + right
        return dfs(root,root.val)
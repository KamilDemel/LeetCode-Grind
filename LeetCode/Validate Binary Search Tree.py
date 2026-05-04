class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        def dfs(node,min_val,max_val):
            if not node:
                return True
            if node.val <= min_val:
                return False
            if node.val >= max_val:
                return False
            return dfs(node.left,min_val,node.val) and dfs(node.right,node.val,max_val)
        return dfs(root,float("-inf"),float("inf"))

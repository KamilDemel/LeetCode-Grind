class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        licznik = 0
        wynik = None
        def dfs(node):
            nonlocal licznik, wynik
            if not node or wynik is not None:
                return
            dfs(node.left)
            licznik += 1
            if licznik == k:
                wynik = node.val
                return
            dfs(node.right)
        dfs(root)
        return wynik
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        max_sum = float("-inf")
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left_node = max(dfs(node.left),0)
            right_node = max(dfs(node.right),0)
            if left_node + right_node + node.val > max_sum:
                max_sum = node.val + left_node + right_node
            return node.val + max(left_node, right_node)
        dfs(root)
        return max_sum





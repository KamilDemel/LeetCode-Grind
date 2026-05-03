class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def diameterofbinarytree(self, root):
        new_record = 0
        def dfs(node):
            nonlocal new_record
            if not node:
                return 0
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            if left_node + right_node > new_record:
                new_record = left_node + right_node
            return 1 + max(left_node,right_node)
        dfs(root)
        return new_record





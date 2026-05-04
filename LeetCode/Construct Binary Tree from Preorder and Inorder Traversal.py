class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        mapa_inorder = {val: idx for idx, val in enumerate(inorder)}
        postorder_idx = len(postorder) - 1
        def build(inorder_start, inorder_end):
            nonlocal postorder_idx
            if inorder_start > inorder_end:
                return None
            szef_val = postorder[postorder_idx]
            szef = TreeNode(szef_val)
            postorder_idx -= 1
            idx_szef = mapa_inorder[szef_val]
            szef.right = build(idx_szef + 1, inorder_end)
            szef.left = build(inorder_start, idx_szef - 1)
            return szef
        return build(0, len(inorder) - 1)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        mapa_inorder = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0
        def build(inorder_start, inorder_end):
            nonlocal preorder_idx
            if inorder_start > inorder_end:
                return None
            szef_val = preorder[preorder_idx]
            szef = TreeNode(szef_val)
            preorder_idx += 1
            idx_szef = mapa_inorder[szef_val]
            szef.left = build(inorder_start, idx_szef - 1)
            szef.right = build(idx_szef + 1, inorder_end)
            return szef
        return build(0, len(inorder) - 1)
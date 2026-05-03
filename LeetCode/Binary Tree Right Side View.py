import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        kolejka = collections.deque()
        res = []
        if not root:
            return res
        kolejka.append(root)
        while kolejka:
            rozmiar = len(kolejka)
            last = kolejka[-1]
            res.append(last.val)
            for _ in range(rozmiar):
                curr_node = kolejka.popleft()
                if not curr_node.left and not curr_node.right:
                    continue
                if curr_node.left and curr_node.right:
                    kolejka.append(curr_node.left)
                    kolejka.append(curr_node.right)
                    continue
                if not curr_node.left and curr_node.right:
                    kolejka.append(curr_node.right)
                    continue
                if curr_node.left and not curr_node.right:
                    kolejka.append(curr_node.left)
                    continue
        return res
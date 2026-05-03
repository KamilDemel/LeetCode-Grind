import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        kolejka = collections.deque()
        res = []
        if not root:
            return res
        res.append([root.val])
        kolejka.append(root)
        while kolejka:
            rozmiar = len(kolejka)
            wynik = []
            for _ in range(rozmiar):
                curr_node = kolejka.popleft()
                if not curr_node.left and not curr_node.right:
                    continue
                if curr_node.left and curr_node.right:
                    wynik.append(curr_node.left.val)
                    wynik.append(curr_node.right.val)
                    kolejka.append(curr_node.left)
                    kolejka.append(curr_node.right)
                    continue
                if not curr_node.left and curr_node.right:
                    wynik.append(curr_node.right.val)
                    kolejka.append(curr_node.right)
                    continue
                if curr_node.left and not curr_node.right:
                    wynik.append(curr_node.left.val)
                    kolejka.append(curr_node.left)
                    continue
            if wynik:
                res.append(wynik)
        return res




import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        def bfs(node1,node2):
            kolejka = collections.deque()
            kolejka.append(node1)
            kolejka.append(node2)
            while kolejka:
                curr_node_1 = kolejka.popleft()
                curr_node_2 = kolejka.popleft()
                if not curr_node_1 and not curr_node_2:
                    continue
                if not curr_node_1 and curr_node_2:
                    return False
                if not curr_node_2 and curr_node_1:
                    return False
                if curr_node_1.val != curr_node_2.val:
                    return False
                kolejka.append(curr_node_1.left)
                kolejka.append(curr_node_2.left)
                kolejka.append(curr_node_1.right)
                kolejka.append(curr_node_2.right)
            return True
        if bfs(p,q):
            return True
        return False


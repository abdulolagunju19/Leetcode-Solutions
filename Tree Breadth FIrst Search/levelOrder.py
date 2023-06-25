
from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Optimal Time Complexity: O(n)
    Space Complexity: O(n/2) = O(n)
        - Algorithm: Conduct BFS with queue for each level, pop it into output list and add the children
    """
    def levelOrder(self, root):
        q = deque()
        q.append(root)
        result = []
        while q:
            qLen = len(q)
            currList = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    currList.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if currList:
                result.append(currList)
        return result


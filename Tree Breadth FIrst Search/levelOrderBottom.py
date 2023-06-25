# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    """
    Optimal Time Complexity: O(n)
    Space Complexity: O(n/2) = O(n)
        - Algorithm: Conduct BFS with queue for each level, pop it into output list at left and add the children
    """
    def levelOrderBottom(self, root) -> list[list[int]]:
        q = deque()
        q.append(root)
        result = deque()
        while q:
            currList = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    currList.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if currList:
                result.appendleft(currList)
        return result


from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    """
    Optimal Time Complexity: O(n)
    Corresponding Space Complexity: O(n/2) = O(n)
        - Algorithm: add node and level to queue, check if theres no children then return level
    """
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root, 1))
        while q:
            node, level = q.popleft()
            if not node.left and not node.right:
               return level
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return level
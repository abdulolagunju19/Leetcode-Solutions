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
        - Algorithm: Conduct BFS with queue for each level, zigzag with bool from level
    """
    def zigzagLevelOrder(self, root) -> list[list[int]]:
        q = deque()
        result = []
        q.append(root)
        leftRight = True
        while q:
            qLen = len(q)

            currList = deque()
            for i in range(qLen):
                node = q.popleft()
                if node:
                    if leftRight:
                        currList.append(node.val)
                    else:
                        currList.appendleft(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if currList:
                result.append(currList)
            leftRight = not leftRight
        return result


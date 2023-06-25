 Definition for a binary tree node.
 class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    """
    Optimal Time Complexity: O(n) where n is the number of nodes
    Corresponding Space Complexity: O(h) where h is the height of the tree
        - Algorithm: use dfs and check sum at leaf nodes
    """
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if (not root.left and not root.right) and root.val == targetSum:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

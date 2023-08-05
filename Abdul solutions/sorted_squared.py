class Solution:
    """
        Runtime Complexity: O(nlogn) time complexity
        Algorithm: Square every value then sort it.
    """
    def sortedSquares(self, nums):
        squared = []
        for i in range(len(nums)):
            squared.append(nums[i]**2)
        squared.sort()
        return squared
    

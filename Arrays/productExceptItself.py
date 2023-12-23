class Solution(object):
    """
        Time complexity: O(2*n) = O(n)
        Space complexity: O(1)

        Algorithm: Compute pre and postfix products for each element then multiply them
    """
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = [1] * len(nums)
        preP, postP = 1, 1
        for i in range(1, len(nums)):
            preP *= nums[i - 1]
            result[i] = preP
        for i in range(len(nums) - 2, -1, -1):
            postP *= nums[i + 1]
            result[i] *= postP
        return result
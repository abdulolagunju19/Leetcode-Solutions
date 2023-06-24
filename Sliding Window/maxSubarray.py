
class Solution:
    """
    Optimal Time Complexity: O(n)
        - Algorithm: traverse array, if the currentSum is below 0 disregard it and start from the next value
    """
    def maxSubArray(self, nums: list[int]) -> int:

        maxSum = nums[0]
        currSum = 0
        for i in range(len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]

            if maxSum < currSum:
                maxSum = currSum
        return maxSum
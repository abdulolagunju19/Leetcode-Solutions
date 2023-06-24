class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Optimal Time Complexity: O(n)
            - Algorithm: sliding window, add till target then check min and move start pointer up
        """
        start, currSum = 0, 0
        minLen = float("inf")

        for end in range(len(nums)):
            currSum += nums[end]
            while currSum >= target:
                currLen = end - start + 1
                minLen = min(currLen, minLen)
                currSum -= nums[start]
                start += 1
        return 0 if minLen == float("inf") else minLen

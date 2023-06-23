class Solution:
    """
    Time complexity: O(nlogn) + O(n^2)
        - Algorithm: sort then select one index then use two sum for each el in list, avoid dupes with while loop
    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        start = 0
        sol = []
        while (start < len(nums) - 2):
            l = start + 1
            r = len(nums) - 1
            target = 0 - nums[start]
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                elif currSum == target:
                    currSol = (nums[start], nums[l], nums[r])
                    sol.append(currSol)
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1

            while start + 1 < len(nums) - 2 and nums[start] == nums[start + 1]:
                start += 1
            start += 1
        return sol

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Runtime Complexity: O(n)
        Space Complexity: O(1)
        Algorithm: Use two pointers, with a slow and fast pointer
        """
        slow = 0
        
        for fast in range(len(nums)):
            if(nums[fast] != 0):
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            
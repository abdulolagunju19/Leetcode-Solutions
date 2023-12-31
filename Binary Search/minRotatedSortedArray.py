class Solution(object):
    """
    Time Complexity: O(logn)
    Space: O(1)
    Algo:
        - compare nuns at mid and left pointer
        - if mid is less then search the left half eg. [4,  1, 2 ,3]
        - otherwise search right half
        - also check whether already sorted so you can just compare leftmost
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        minNum = nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[r] > nums[l]:  # already sorted
                return min(minNum, nums[l])
            minNum = min(minNum, nums[mid])
            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        return minNum

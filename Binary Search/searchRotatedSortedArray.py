class Solution(object):
    """
    Time complexity: O(logn)
    Space: O(1)
    Algo:
        - Run binary search on sorted portions of the array
        - if left is sorted then arr[mid] >= arr[l] as the pivot must be in right side eg. [3,4,5,6,0,1,2]
            - check whether target is in range of sorted otherwise check unsorted
        - if arr[mid] < arr[l] then right is sorted as pivot must be in left portion eg. [6,0,1,2,3,4,5]
            - check whether target is in range of sorted otherwise check unsorted
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid + 1] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return -1

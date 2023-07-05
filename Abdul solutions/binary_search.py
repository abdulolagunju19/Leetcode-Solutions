class Solution:
    """
    Runtime Complexity: O(n), iterate through while loop
    Space Complexity: O(1), only need low and high and mid variable
    Algorithm: Look for middle element, check if it is bigger or smaller    than target, create new left and right pointer
    """
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while(low <= high):
            mid = (low + high) // 2

            if(nums[mid] < target):
                low = mid + 1
            elif(nums[mid] > target):
                high = mid - 1
            else:
                return mid
        return -1
class Solution:
    """
    Runtime Complexity: O(n^2) due to for and while loop
    Space Complexity: O(1)?
    Algorithm: Use two pointers to find two numbers to make sum
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if (nums[i - 1] == nums[i] and i > 0):
               continue
            left = i + 1
            right = len(nums) - 1

            while(left < right):
                threeSum = nums[i] + nums[left] + nums[right]
                if(threeSum < 0):
                    left += 1
                elif(threeSum > 0):
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while(left < right and nums[left] == nums[left-1]):
                        left += 1
        return triplets


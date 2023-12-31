class Solution(object):
    """
    Time complexity: O(n)
    Space: O(1)
    Algorithm:
        - Greedy algo where we choose the one with the highest height to keep
        - move the pointer of the min b/w r and l
        - that way we keep the highest area as its limited by the lowest height
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxWater = 0
        while l < r:
            currWater = min(height[l], height[r]) * (r - l)
            maxWater = max(maxWater, currWater)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxWater



class Solution:
    """
    Runtime Complexity: O(n), go through while loop n times
    Space Complexity: O(1)
    Algorithm: Sliding window, left point and right pointer start next to each other
    """
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        left = 0
        right = 1
        while(left < right and right < len(prices)):
            if(prices[right] - prices[left] < 0):
                left = right
                right += 1
            else:
                if(maximum < prices[right] - prices[left]):
                    maximum = prices[right] - prices[left]
                right += 1
        return maximum
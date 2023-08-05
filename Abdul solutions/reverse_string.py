class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        Runtime Complexity: O(n)
        Space Complexity: O(1)
        Algorithm: Use two pointers, one at the beginning and one at the end
        """
        left = 0

        right = len(s) - 1

        while (left < right):
            s[left], s[right] = s[right], s[left]

            left +=1
            right -= 1
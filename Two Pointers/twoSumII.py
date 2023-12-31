class Solution:
    """
    Optimal Time Complexity: O(n)
        - Algorithm: use two pointers, if the sum > target then move right down else move left down
    """
    def twoSumII(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            nSum = numbers[i] + numbers[j]
            if nSum < target:
                i += 1
            elif nSum > target:
                j -= 1
            else:
                return i + 1, j + 1

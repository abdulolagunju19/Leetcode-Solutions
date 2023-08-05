class Solution:
    """
    Runtime Complexity: O(n) or O(n^2)? checking if number is in other list?
    Space Complexity: O(n)
    Algorithm: check if number in one list is in other list, if it is, add to hashset
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = set()
        
        for i in range(len(nums1)):
            if(nums1[i] in nums2):
                hashset.add(nums1[i])
        return hashset
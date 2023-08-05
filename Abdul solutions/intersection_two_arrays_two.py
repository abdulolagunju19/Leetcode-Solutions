class Solution:
    """
    Runtime Complexity: O(n) there are no nested loops, the in keyword for a dict is O(1)
    Space Complexity: O(n) because intersection may contain all elements in list
    Algorithm: store frequency of numbers in first list in hashmap, then add to intersection list if number exists in the other list and decrement the frequency in the dictionary
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        intersection = []

        for i in range(len(nums1)):
            if (nums1[i] in count):
                count[nums1[i]] += 1
            else:
                count[nums1[i]] = 1

        for i in range(len(nums2)):
            if(nums2[i] in count and count[nums2[i]] > 0):
                count[nums2[i]] -= 1
                intersection.append(nums2[i])
        return intersection
        
                
class Solution:
    """
    Algorithm:
    - create hashmap of the frequencies of each number
    - make a list with same size as input array, this list will have the frequencies as the index
    - go through hashmap and store each number at their frequency index in the list
    - iterate through list from the end and stop when you have k elements in result

    Time complexity: O(n *3) = O(n)
    Space: O(n * 2) = O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        result = []
        for i in nums:
            freqDict[i] = 1 + freqDict.get(i, 0)
        numsList = [[] for i in range(len(nums) + 1)]
        for val in freqDict:
            numsList[freqDict[val]].append(val)
        count = 0
        for i in range(len(numsList) - 1, 0, -1):
            for num in numsList[i]:
                if count == k:
                    return result
                result.append(num)
                count += 1
        return result
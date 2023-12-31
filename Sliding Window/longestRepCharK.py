class Solution(object):
    """
    Time Complexity: O(n)
    Space: O(26) = O(1)
    Algo:
        - sliding window keep track of maxFrequency in window
        - if maxFreq + k is less than the current window means we need to check others so we increase left
        - its alright if maxF overestimates as we only care about the longest substring
    """
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freqDict = {}
        l = 0
        maxSub = 0
        maxF = 0
        for r in range(len(s)):
            freqDict[s[r]] = 1 + freqDict.get(s[r], 0)
            maxF = max(maxF, freqDict[s[r]])
            while maxF + k < r - l + 1:
                freqDict[s[l]] -= 1
                l += 1
            maxSub = max(r - l + 1, maxSub)
        return maxSub



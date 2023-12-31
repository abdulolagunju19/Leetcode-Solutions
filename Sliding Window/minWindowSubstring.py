class Solution(object):
    """
    Time Complexity: O(n+m)
    Space: O(t)
    Algo:
        - based on comparing our windows frequencies to required frequencies
        - Store the required matches needed which comes from t's freqDict as we will check whether we meet the condition
        - Run through string and update our currMatches checking whether its equal to required Matches
        - if we meet the conditions shrink the substring from the left, updating currMatches
        - when we don't increase right pointer
    """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        currMatches = 0
        currDict, tDict = {}, {}
        l = 0
        minWin = ""
        for char in t:
            tDict[char] = 1 + tDict.get(char, 0)
        reqMatches = len(tDict)
        for r in range(len(s)):
            if s[r] in tDict:
                currDict[s[r]] = 1 + currDict.get(s[r], 0)
                if currDict[s[r]] == tDict[s[r]]:
                    currMatches += 1
                    while currMatches == reqMatches:
                        if len(minWin) > r - l + 1 or minWin == "":
                            minWin = s[l:r + 1]
                        if s[l] in tDict:
                            currDict[s[l]] = currDict.get(s[l]) - 1
                            if currDict[s[l]] < tDict[s[l]]:
                                currMatches -= 1
                        l += 1
        return minWin




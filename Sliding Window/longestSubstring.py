class Solution(object):
    """
    Time: O(n)
    Space: O(n)
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxSub = 0
        strSet = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] in strSet:
                strSet.remove(s[l])
                l += 1
            else:
                strSet.add(s[r])
                maxSub = max(r - l + 1, maxSub)
                r += 1
        return maxSub

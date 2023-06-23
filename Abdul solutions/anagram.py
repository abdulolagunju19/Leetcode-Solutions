def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    if countS != countT:
        return False
    return True
"""
def isAnagram(self, s, t):
    first_string = sorted(s)
    second_string = sorted(t)

    if (first_string == second_string):
        return True
    return False
"""
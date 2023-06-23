def isAnagram(self, s: str, t: str) -> bool:
    """
    Optimal Time complexity: O(s+t) = O(n)
        - Algorithm: create hashmap for s and t with initial frequency of 1
                    - compare hashmap return false if not equal
    """
    countS, countT = {}, {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
def isAnagram_space(self, s: str, t: str) -> bool:
    """
    Optimal Space complexity: O(26) = O(1)
        - Algorithm: sort both strings and compare them
    :param self:
    :param s:
    :param t:
    :return:
    """
    return sorted(s) == sorted(t)


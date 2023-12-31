class Solution(object):
    """
    Time complexity: O(n)
    Space: O(n)
    Algo:
        - store open brackets in stack, pop them and compare when you see a closing bracket
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            ')': '(' ,
            ']': '[',
            '}': '{',
        }
        stack = []
        count = 0
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                openB = stack.pop()
                if openB != brackets[char]:
                    return False
        return len(stack) == 0
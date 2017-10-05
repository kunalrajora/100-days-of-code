class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for p in s:
            if p in lookup:
                stack.append(p)
            elif len(stack) == 0 or lookup[stack.pop()] != p:
                return False
        return len(stack) == 0

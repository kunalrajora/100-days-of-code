class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        z = False
        if x < 0:
            x = str(x)
            if x == x[:0:-1]:
                z = True
        else:
            x = str(x)
            if x == x[::-1]:
                z = True
        return z

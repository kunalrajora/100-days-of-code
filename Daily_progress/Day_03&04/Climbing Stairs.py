class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = s = 1
        for _ in range(n):
            f, s = s, f + s
        return f

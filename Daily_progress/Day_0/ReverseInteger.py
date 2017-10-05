class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        z = ""
        if x >= 0:
            x = str(x)
            z = x[::-1]
            if int(z) > 2147483647:
                z = 0
        else:
            x = str(x)
            z = x[0] + x[:0:-1]
            if int(z[1:]) > 2147483647:
                z = 0
        return int(z)

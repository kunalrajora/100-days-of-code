class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x > y:
            x = bin(x)[2:][::-1]
            y = bin(y)[2:][::-1]
            z = len(x) - len(y)
            y = y + '0' * z
        else:
            x = bin(x)[2:][::-1]
            y = bin(y)[2:][::-1]
            z = len(y) - len(x)
            x = x + '0' * z
        count = 0

        for i in range(min(len(x), len(y))):
            if x[i] != y[i]:
                count += 1
        return count

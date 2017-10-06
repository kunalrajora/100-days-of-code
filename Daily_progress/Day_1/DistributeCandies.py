class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        x = len(set(candies))
        y = len(candies) // 2
        if x == y:
            return x
        elif x > y:
            return y
        else:
            return x

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if (len(nums[0]) * len(nums)) != (r * c):
            return nums

        one = sum(nums, [])
        final = []
        start = 0
        end = 0
        for i in range(r):
            if i > 0:
                start += c
            end += c
            final.append(one[start:end])
        return final

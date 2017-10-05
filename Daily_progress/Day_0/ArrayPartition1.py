class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = sorted(nums)
        n = 2
        nums = [l[i:i + n] for i in range(0, len(l), n)]
        final = []
        for i in range(len(nums)):
            final.append(min(nums[i]))
        return sum(final)

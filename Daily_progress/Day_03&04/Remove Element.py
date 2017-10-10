class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c = nums.count(val)
        for i in nums:
            if i == val:
                while c != 0:
                    c -= 1
                    nums.remove(val)
        return len(nums)

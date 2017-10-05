class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        li = []
        for i in range(len(nums) - 1):
            x = target - nums[i]
            y = nums[i]
            nums.pop(i)
            if x in nums:
                li = [i, (nums.index(x)) + 1]
                break
            nums.insert(i, y)
        return sorted(li)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums=sorted(nums)
        for n in range(len(nums)-1):
            if nums[n]==nums[n+1]:
                return True
        return False
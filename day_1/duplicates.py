class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(nums) != len(set(nums)):
        #     return True
        # return False
        return True if len(set(nums)) != len(nums) else False
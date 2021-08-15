"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l,r = 0, len(nums)-1

        while l < r:
            curr_sum = nums[l] + nums[r]

            if curr_sum > target:
                r-=1
            elif curr_sum < target:
                l+=1
            else:
                return [l+1,r+1]
        return []
        





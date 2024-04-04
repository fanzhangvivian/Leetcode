#
# @lc app=leetcode id=2824 lang=python
#
# [2824] Count Pairs Whose Sum is Less than Target
#

# @lc code=start
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if (nums[left] + nums[right] < target):
                count += right - left
                left += 1
            else:
                right -= 1
        return count
# @lc code=end


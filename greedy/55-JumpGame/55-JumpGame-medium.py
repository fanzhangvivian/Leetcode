#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Greedy: Always extending the reach (cover) as far as possible with each step.
        # each step is to find the most cover range and update it
        # update the cover: find the farthest index between you the current reach and past reach
        # if cover range is >= last index, return true.
        cover = 0
        i = 0
        if len(nums) == 1:
            return True
        while i <= cover:
            cover = max(i+nums[i], cover)
            if cover >= len(nums)-1:
                return True
            i += 1
        return False
# @lc code=end


#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#

# @lc code=start
from functools import cache


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if sums of all positive numbers = p, sums of all negative numbers = s-p, s represent all the nums's sum
        # then we can get p-(s-p) = target 
        # so p = (target+s)/2

        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0
        m = s // 2

        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]: # item's value>target value
                return dfs(i-1, c) # dont choose the number
            return dfs(i-1, c) + dfs(i-1, c-nums[i]) # choose the number and don't choose

        return dfs(len(nums)-1, m)

# @lc code=end


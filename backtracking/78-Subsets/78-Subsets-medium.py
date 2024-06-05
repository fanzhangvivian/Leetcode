#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        result = []
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startindex, path, result):
        result.append(path[:])
        if startindex >= len(nums):
            return
        for i in range(startindex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()

# @lc code=end


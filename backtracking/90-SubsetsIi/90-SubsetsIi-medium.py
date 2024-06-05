#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        path = []
        result = []
        used = [False] * len(nums)
        nums.sort()
        self.backtracking(nums, 0, used, path, result)
        return result

    def backtracking(self, nums, startindex, used, path, result):
        result.append(path[:])
        for i in range(startindex, len(nums)) :
            if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, i+1, used, path, result)
            used[i] = False
            path.pop()
# @lc code=end


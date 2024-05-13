#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(candidates, target, result, [])
        return result
    
    def backtracking(self, candidates, target, result, path):
        if sum(path) > target:
            return
        if sum(path) == target:
            result.append(path[:])
            return
        for i in range(len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates[i:], target, result, path)
            path.pop()
# @lc code=end


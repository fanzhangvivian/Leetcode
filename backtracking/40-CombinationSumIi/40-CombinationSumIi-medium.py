#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.backtracking(candidates, target, result, [])
        return result
    
    def backtracking(self, candidates, target, result, path):
        if sum(path) > target:
            return
        if sum(path) == target:
            result.append(path[:])
            return
        
        for i in range(len(candidates)):
            if i > 0:
                if candidates[i] == candidates[i-1]:
                    continue
            path.append(candidates[i])
            self.backtracking(candidates[i+1:], target, result, path)
            path.pop()
# @lc code=end


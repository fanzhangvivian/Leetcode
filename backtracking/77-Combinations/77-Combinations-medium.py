#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = [] # 2d array
        self.backtracking(n, k, 1, [], result)
        return result
    
    def backtracking(self, n, k, startindex, path, result):
        if len(path) == k:
            result.append(path[:])
            return 
        for i in range(startindex, n+1):
            path.append(i)
            self.backtracking(n, k, i+1, path, result)
            path.pop()


        
# @lc code=end


#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtacking(k, n, 1, [], result)
        return result
    
    def backtacking(self, k, n, startindex, path, result):
        # Pruning: When finding the sum is greater than n, it stoped searching
        if sum(path) > n:
            return
        # base case: When finding the sum is equal to the target n, and lenght of 
        # the path is equal to k, the right path should be add into the result.
        if len(path) == k and sum(path) == n:
            result.append(path[:])
            return
        # Range pruning: the range should not be greater than 9-(k-len(path))+1
        for i in range(startindex, 9-(k-len(path))+2):
            path.append(i)
            self.backtacking(k, n, i+1, path, result)
            path.pop()

# @lc code=end


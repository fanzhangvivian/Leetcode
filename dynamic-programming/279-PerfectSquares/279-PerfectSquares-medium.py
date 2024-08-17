#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the same solution with 322 coins_change

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, int(n ** 0.5) + 1): #iterate the item: square of n
            for j in range(i * i, n + 1): # iterate the package 
                dp[j] = min(dp[j-i*i] + 1, dp[j])
        
        return dp[n]

# @lc code=end


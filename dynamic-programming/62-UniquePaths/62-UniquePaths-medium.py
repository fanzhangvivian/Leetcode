#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # set a array to store the unique path of each column
        # there is only one way to reach any cell in the first row (by moving right).
        dp = [1] * n

        # Calculate the unique path of each cell
        # Iterate the outer loop from the second row
        for j in range(1, m):
            # The inner loop iterates over columns starting from the second column
            for i in range(1, n):
                dp[i] += dp[i-1]

        return dp[n-1]
        
# @lc code=end


#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # bullet point: when the obstacle is in the first row/column, the path numbers of next cell after
        # the obstacle will still be 0
        # 1.edge case: if the obstacle is in bottom-right corner/ top-left corner, return 0
        # 2.Initialize a 2d table array and set all value to 0
        # define the dp[i][j], it represents the start from index[0][0]to the bottom[i][j] we have dp[i][j] numbers path
        # 3.Determine the recurrence formula: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 4. Initialize the First Column and first row. Until an obstacle is encountered, we set dp[i][0] = 1
        # 5.  iterate over the rest of the grid:a.if it is not an obstacle, we set  dp[i][j] = dp[i-1][j] + dp[i][j-1];b.we skip it
        # 6. return the result

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]




    
# @lc code=end


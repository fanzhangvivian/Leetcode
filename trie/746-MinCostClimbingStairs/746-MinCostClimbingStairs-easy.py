#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 1.create the dp table
        # 2. Initialize the dp[0] and dp[1] cuz we can choose from index[0] or index[1] without any expense
        # 3. Traverse from front to back and find the minimum cost of dp[i] + cost[i]
        n = len(cost) 
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], cost[i-2] + dp[i-2])
        
        return dp[n]


# @lc code=end


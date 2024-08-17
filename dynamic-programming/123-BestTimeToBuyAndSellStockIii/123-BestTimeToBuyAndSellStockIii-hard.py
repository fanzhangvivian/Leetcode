#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 1. Initialize a dp array dp[i][j] represents the maximum profit on day i in the j-th state.
        # 2. Defination： dp[i][0]: No operation (this state can be omitted).
        # dp[i][1]: Maximum profit after the first buy.（第一次持有）
        # dp[i][2]: Maximum profit after the first sell.（第一次不持有）
        # dp[i][3]: Maximum profit after the second buy. （第二次持有）
        # dp[i][4]: Maximum profit after the second sell. （第二次不持有）
        # 3. Recursive Formula

        if len(prices) == 0:
            return 0
        dp = [[0] * 5 for _ in range(len(prices))]

        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

        return dp[-1][4]
# @lc code=end


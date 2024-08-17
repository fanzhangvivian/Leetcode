#
# @lc app=leetcode id=714 lang=python
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # Similar to question 122 but subtracting the fee

        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)

        return max(dp[-1][0], dp[-1][1]) # 这里不是直接返回不持有股票的状态，有可能卖出股票后手续费更高，所以要取最大值

# @lc code=end


#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # create a 2d DP table;
        # 2. Defination:dp[i][0] represents the maximum profit on day i when holding a stock.
        # dp[i][1] represents the maximum profit on day i when not holding a stock.
        # 3. Recursive Formula: 1) The maximum profit on day i when holding a stock depends on two scenarios: dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
        # a. Continuing to hold the stock from the previous day, which is dp[i-1][0].
        # b. Buying the stock on day i, which is the profit from not holding a stock on the previous day minus the cost of the stock on day i, which is dp[i-1][1] - prices[i].
        # 2) dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i]): The maximum profit on day i when not holding a stock depends on two scenarios:
        # a.Continuing to not hold a stock from the previous day, which is dp[i-1][1].
        # b. Selling the stock on day i, which is the profit from holding a stock on the previous day plus the price of the stock on day i, which is dp[i-1][0] + prices[i]
        # 4. Initialize: dp[0][0] = -price[0] (the profit is negative because of the cost of the stock)
        # dp[0][1] = 0 (means not holding any stock on the first day, so the profit is zero)

        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        return dp[-1][1]


# @lc code=end


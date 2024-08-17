#
# @lc app=leetcode id=188 lang=python
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # 1.Initialize the dp array: dp[i][j] represents the maximum profit on day i after j transactions
        # one trancsactions represents one buy and one sell, so it should be 2k+1
        # Initialize the states where we hold stock after the first buy, third buy, etc., with -prices[0] on the first day
        # 2. Defination:dp[i][j+1]: represents the state after buying for the j/2 + 1 time. like dp[i][1] when j=0
        # dp[i][j+2]: represents the state after selling for the j/2 + 1 time. like dp[i][2] when j=0
        # 3. Recursive Formula: 
        # 1).dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i]): The maximum profit after buying for the j/2 + 1 time is the maximum of:
        # a.Continuing to hold the stock from the previous state.
        # b.Buying the stock on day i, which is the profit from the previous sell minus the cost of the stock on day i.
        # 2)dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i]): The maximum profit after selling for the j/2 + 1 time is the maximum of:
        # a.Continuing to not hold the stock from the previous state.
        # b.Selling the stock on day i, which is the profit from holding the stock plus the price of the stock on day i.
        # 4. Return the state dp[-1][2*k], which represents the maximum profit after k transactions.


        if len(prices) == 0:
            return 0
        dp = [[0] * (2*k + 1) for _ in range(len(prices))]
        for j in range(1, 2*k, 2):
            dp[0][j] = -prices[0] # 初始化所有买出时，持有股票价格

        for i in range(1, len(prices)):
            for j in range(0, 2*k-1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j]-prices[i]) # 当天持有：1保持前一天持有的情况，2当天买入i股票：前一天不持有的价格-i股票的价格
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1]+prices[i]) # 当天不持有：1.保持前一天不持有，2.当天卖出股票：前一天持有的价格+i股票价格

        return dp[-1][2*k]


# @lc code=end


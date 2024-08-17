#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Defination：
        # dp[i][0] hold the stocks 持有股票的那一天
        # dp[i][1] hold the stock state 保持卖出股票状态（前面就卖了一直没操作
        # dp[i][2] sell the stock 具体卖出股票的那一天
        # dp[i][3] cooldown day 冷冻期
        # Recursive Formula：
        # a. dp[i][0] = max(dp[i - 1][0], dp[i - 1][3] - prices[i], dp[i - 1][1] - prices[i])
        # 前一天就是持有股票状态（状态一），dp[i][0] = dp[i - 1][0]
        # 操作二：今天买入了，有两种情况:前一天是冷冻期（状态四），dp[i - 1][3] - prices[i] 和前一天是保持卖出股票的状态（状态二），dp[i - 1][1] - prices[i]
        # b.dp[i][1] 操作一：前一天就是状态二 和前一天是冷冻期（状态四）
        # dp[i][1] = max(dp[i - 1][1], dp[i - 1][3]);
        # c. dp[i][2] ，只有一个操作：昨天一定是持有股票状态（状态一），今天卖出 即：dp[i][2] = dp[i - 1][0] + prices[i];
        # d. dp[i][3] = dp[i - 1][2] 冷冻期 只能是昨天的状态
        # Initialization：dp[0][0] = -prices[0] dp[0][1] = 0 dp[0][2] = 0 dp[0][3]=0

        n = len(prices)
        if n == 0:
            return 0
        dp = [[0]*4 for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], max(dp[i-1][3], dp[i-1][1]) - prices[i]) # 当前持有股票的最大利润等于前一天持有股票的最大利润或者前一天不持有股票且不处于冷冻期的最大利润减去当前股票的价格
            dp[i][1] = max(dp[i-1][1], dp[i-1][3]) #  # 当前不持有股票且处于冷冻期的最大利润等于前一天持有股票的最大利润加上当前股票的价格
            dp[i][2] = dp[i-1][0] + prices[i] # 当前不持有股票且不处于冷冻期的最大利润等于前一天不持有股票的最大利润或者前一天处于冷冻期的最大利润
            dp[i][3] = dp[i-1][2] # 当前不持有股票且当天卖出后处于冷冻期的最大利润等于前一天不持有股票且不处于冷冻期的最大利润
        
        return max(dp[n-1][3], dp[n-1][1], dp[n-1][2]) # 返回最后一天不持有股票的最大利润

# @lc code=end


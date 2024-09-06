#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                if dp[i-coin] != float('inf'):
                    dp[i] = min(dp[i-coin]+1, dp[i])
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
  
# @lc code=end


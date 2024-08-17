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
        # 完全背包问题
        # defination: dp[j] the minimum numbers' item to fill the package
        # formula: dp[j] = min(dp[j-coins[i]] + 1, dp[j]) 
        # Cuz we have 2 ways to fill the amount 1.without the coins[i]),2.with it
        # initialization: dp[0]=0 others: float('inf') (cuz we are looking for the minimum value)

        dp = [float('inf')] * (amount + 1) # Initialize the dp value into float inf
        dp[0] = 0 # Initialize the dp value 0 cuz the amount is 0, the numbers is 0

        for coin in coins: # Iterate the coins(items)
            for i in range(coin, amount+1): # Iterate the amount(package capcity)
                if dp[i-coin] != float('inf'): # if the dp[i-coin] is not initialization, update the amount
                    dp[i] = min(dp[i-coin]+1, dp[i]) 
        
        if dp[amount] == float('inf'): # if the amount is still float, it shows no way to fill it
            return -1
            
        return dp[amount]
 
# @lc code=end


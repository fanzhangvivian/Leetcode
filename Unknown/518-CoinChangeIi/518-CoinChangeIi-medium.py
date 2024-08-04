#
# @lc app=leetcode id=518 lang=python
#
# [518] Coin Change II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        #   完全背包问题
        # 1.dp[i] definition: fill this amount of coins
        # 2. dp formula: dp[j] +=dp[j-coins[i]] 只要搞到coins[i]，凑成dp[j]就有dp[j-coins[i]] 种方法
        # 已经有一个1（nums[i]） 的话，有 dp[4]种方法 凑成 容量为5的背包。
        # 已经有一个2（nums[i]） 的话，有 dp[3]种方法 凑成 容量为5的背包。
        # 已经有一个3（nums[i]） 的话，有 dp[2]种方法 凑成 容量为5的背包
        # 已经有一个4（nums[i]） 的话，有 dp[1]种方法 凑成 容量为5的背包
        # 已经有一个5 （nums[i]）的话，有 dp[0]种方法 凑成 容量为5的背包
        # 那么凑整dp[5]有多少方法呢，也就是把 所有的 dp[j - nums[i]] 累加起来。

        dp = [[0] * (amount + 1) for _ in range(len(coins))]

        # Initialize the first column
        for i in range((len(coins))):
            dp[i][0] = 1 # There's one way to make up amount 0: use no coins
        
        # Initialize the first row
        for j in range(coins[0], amount+1):
            dp[0][j] += dp[0][j-coins[0]] 

        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                if j<coins[i]:
                    dp[i][j] = dp[i-1][j] #  if the amount is less than the coin value, we just use the previous value.
                else:
                    dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j] # we take the sum of using the coin and not using the coin.

        return dp[len(coins)-1][amount]





        
# @lc code=end


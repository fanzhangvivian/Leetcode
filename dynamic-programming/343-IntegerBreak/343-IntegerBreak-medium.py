#
# @lc app=leetcode id=343 lang=python
#
# [343] Integer Break
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bullet point: the integer is breaked into the similar number, 
        # the difference is smaller, the product is bigger
        # 1. dp[i] defination: the maximize product of breaking the i
        # 2. dp formula: dp[i] = j * dp[i-j]
        # 3. dp initialize: dp[1] = 0 dp[2] = 1
        # 4. Iterate order: outer loop from 3 to n-1; inner loop from 1 to (i//2 +1)

        # assume the integer i can be breaked into a first inger j(1<=j< i), two solution of the product:
        # 1) spilt the i into j and i-j, so the product should be j*(i-j)
        # 2) spilt the i into j and i-j, and i-j still continue to be spilt, and the product should be j*dp[i-j]

        dp = [0] * (n+1)
        # Initialize the dp
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1

        for i in range(3, n+1):
            for j in range(1, i//2 + 1):
                # compared with the current dp[i]' value, j with dp(i-j), j with (i-j)
                dp[i] = max(dp[i], (i-j) * j, dp[i-j]*j)

        return dp[n]


# @lc code=end


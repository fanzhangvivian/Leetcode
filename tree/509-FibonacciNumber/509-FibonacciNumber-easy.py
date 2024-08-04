#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. determine the meaning of dp[i]
        # 2. detemine the formula of recursion
        # 3. Intialize the dp array dp[0] = 1 dp[1] = 1
        # 4. determine the traversal order: from front to end
        
        # exclude Corner Case
        if n == 0:
            return 0
        # create the dp table
        dp = [0] * (n+1)
        # Initialize the dp array
        dp[0] = 0
        dp[1] = 1
        # Traverse from the front to back
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]


sol = Solution()
result = sol.fib(5)
print(result)
# @lc code=end


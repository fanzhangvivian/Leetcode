#
# @lc app=leetcode id=474 lang=python
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j]: the maximum numbers of subset of the string with at most i 0 and j 1
        #
        dp = [[0] * (n+1) for _ in range(m+1)] # 创建二维动态规划数组，初始化为0
        for s in strs:
            zeroNum = s.count('0') # 统计0的个数
            oneNum = s.count('1') # 统计1的个数
            for i in range(m, zeroNum-1, -1): # 遍历背包容量且从后向前遍历
                for j in range(n, oneNum-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum] + 1)
        return dp[m][n]
# @lc code=end


#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 如果 s 是s与t的最长公共子序列，则为true
        # if the s is longest comman subarray of t, return true
        # dp[i][j] : 2d array end with index[i-1] of s and end with index[j-1] of t
        # 以i-1，j-1结尾方便第一行，第一列初始化为0
        # Recursive forma: 1.compare s[i-1] with t[j-1], if it is equal, dp[i][j] = dp[i-1][j-1] + 1
        # 2 if it is not equal, 要删掉t中的前一位去比较s，so dp[i][j] = dp[i][j-1]
        # Initialize first row and column dp[i][0], dp[0][j] = 0
        # Iterate order: from left to right and from top to buttom

        dp = [([0] * (len(t) + 1)) for _ in range(len(s) + 1)]

        maxlength = 0

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
                if dp[i][j] > maxlength:
                    maxlength = dp[i][j]

        if maxlength == len(s):
            return True
        else:
            return False
# @lc code=end


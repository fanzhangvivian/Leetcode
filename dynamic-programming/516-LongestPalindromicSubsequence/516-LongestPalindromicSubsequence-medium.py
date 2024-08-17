#
# @lc app=leetcode id=516 lang=python
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Defination: dp[i][j]: longest palindrome subsequence of index from [i,j] of string
        # Recursive Formula:if s[i]==s[j]: we can iterate from i+1 to j-1, and length +2 向里继续搜索
        # if s[i]!=s[j], we can consider from(i,j-1) or from(i+1, j) 向里继续搜索
        # Initialize：if i==j, we should initialize dp[i][i]=1 它本身是一个回文
        # Iterate order:from button to top and from left to right

        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1): # from button to top
            for j in range(i+1, len(s)): # from left to right and we don't need to iterate i=j situation 
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]


# @lc code=end


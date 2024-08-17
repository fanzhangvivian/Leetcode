#
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # dp[i][j]: Longest Common Subsequence of start from 0-i-1 of text1 and from 0-i-2 of text2
        # Recursive forma: if text1[i] == text2[j], we can continue interate and length+1
        # if text[i] != text2[j], consider the dp[i-1][j] or dp[i][j-1] and get the maxlength
        # Initialize the 2d array. dp[i][0] and dp[0][j] = 0
        # Iterate order:
        # create a 2d array

        dp = [([0] * (len(text2) + 1)) for _ in range(len(text1) + 1)]

        result = 0

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                # The length of the longest common subsequence at the current 
                # position is the value from the top-left diagonal position plus one.
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # if they are not equal, the length of the longest 
                # common subsequence at the current position is the greater value between the top and left positions.
                elif text1[i-1] != text2[j-1]:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                if dp[i][j] > result:
                    result = dp[i][j]
        return result
# @lc code=end


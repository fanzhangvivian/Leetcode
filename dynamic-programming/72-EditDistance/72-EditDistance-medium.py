#
# @lc app=leetcode id=72 lang=python
#
# [72] Edit Distance
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j]: minimum operations of end with [i-1] of word1 and [j-1]of word2
        # if word1[i-1]=word2[j-1] dp[i][j]=dp[i-1][j-1]
        # if word1[i-1]!=word2[j-1]: 1.delete operation word2删除1个元素或者word1删除1个元素 dp[i-1][j] or dp[i][j-1] 增加1此操作
        # 2.replacement替换 换1个元素（增加1次操作），则可以让两者相同，dp[i][j]=dp[i-1][j-1] + 1
        # Initialize dp[i][0]= i and dp[0][j] = j 操作i/j次，变为另外一个字符
        # iterate order: from left to right, and then from top to button
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(len(word2)+1):
            dp[0][i] = i
        for j in range(len(word1)+1):
            dp[j][0] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
        
        return dp[-1][-1]

# @lc code=end


#
# @lc app=leetcode id=583 lang=python
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 1st solution:
        # dp[i][j]: the minimum operations of finding (end with index[i-1] of word1 and end with index[j-1] of word2）
        # if word[i-1] = word2[j-1],the operation of dp[i][j] == dp[i-1][j-1] cuz 2 element is same, we don't need any opearations
        # if word1[i-1] != word2[j-1], the dp[i][j]=dp[i-1][j]+1(我们需要删除word1中一个元素，所以操作次数+1)，同理或则dp[i][j]=dp[i][j-1]+1
        # 或者两者都删除，所以操作＋2 dp[i][j]=dp[i-1][j-1]+2

        # 2nd solution: find the longest comman subarray = n, len(word1)+len(word2) - 2*n =result
        # 2个字符串长度相加减去公共子序列长度*2 就等于最小操作次数


        # 2nd solution
        dp = [([0] * (len(word2) + 1)) for _ in range(len(word1) + 1)]

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        maxSubarrayLength = dp[len(word1)][len(word2)]

        result = len(word1) + len(word2) - (maxSubarrayLength * 2)

        # 1st solution
        dp = [([0] * (len(word2)+1)) for _ in range(len(word1) + 1)]

        for i in range(len(word1)+1): # when the word2 is empty,we should delet all the element in word1
            dp[i][0] = i 
        for j in range(len(word2)+1): # # when the word1 is empty,we should delet all the element in word2
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+2)
        return dp[len(word1)][len(word2)]




# @lc code=end


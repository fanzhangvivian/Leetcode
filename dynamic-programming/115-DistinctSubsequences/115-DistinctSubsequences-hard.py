#
# @lc app=leetcode id=115 lang=python
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp[i][j]: 2D arrays
        # s 删除哪些元素 可以变成t 所以考虑删掉一个元素或者匹配当前元素
        # 如果元素不匹配，则应该从s中删除一个元素继续比较

        dp = [([0] * (len(t) + 1)) for _ in range(len(s) + 1)]
        # result = 0
        for i in range(len(s)):
            dp[i][0] = 1
        for j in range(1, len(t)):
            dp[0][j] = 0
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

                # if dp[i][j] > result:
                #     result = dp[i][j]
        return dp[-1][-1]



# @lc code=end


#
# @lc app=leetcode id=97 lang=python
#
# [97] Interleaving String
#

# @lc code=start
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # 1. 初始化 s1,s2,s3 的长度分别为 len1,len2,len3
        # 2. 若 len1+len2!=len3，表示一定不能构成交错字符串，返回 False
        # 3. 初始化 dp 为 (len1+1)∗(len2+1) 的 False 数组。
        # 初始化第一列 dp[i][0]，遍历第一列，遍历区间 [1,len1+1)：
        # dp[i][0]=dp[i−1][0]ands1[i−1]==s3[i−1]。表示 s1 的前 i 位是否能构成 s3 的前 i 位。因此需要满足的条件为，前 i−1 位可以构成 s3 的前 i−1 位且 s1 的第 i 位（s1[i−1]）等于 s3 的第 i 位（s3[i−1]）
        # 初始化第一行 dp[0][j]，遍历第一行，遍历区间 [1,len2+1)：
        # dp[0][i]=dp[0][i−1]ands2[i−1]==s3[i−1]。表示 s2 的前 i 位是否能构成 s3 的前 i 位。因此需要满足的条件为，前 i−1 位可以构成 s3 的前 i−1 位且 s2 的第 i 位（s2[i−1]）等于 s3 的第 i 位（s3[i−1]）
        # 4. 遍历 dp 数组，每一行 i，遍历区间 [1,len1+1)：
        # 每一列 j，遍历区间 [1,len2+1)：
        # dp[i][j]=(dp[i][j−1] and s2[j−1]==s3[i+j−1]) or (dp[i−1][j] and s1[i−1]==s3[i+j−1]) 。
        # 解释：s1 前i 位和 s2 的前 j 位能否组成 s3 的前 i+j 位取决于两种情况：
        # s1 的前 i−1 个字符和 s2 的前 j 个字符能否构成 s3 的前 i+j−1 位，且 s1 的第 i 位（s1[i−1]）是否等于 s3 的第 i+j 位（s3[i+j−1]）。
        # s1 的前 i 个字符和 s2 的前 j−1 个字符能否构成 s3 的前 i+j−1 位，且 s2 的第 j 位（s2[j−1]）是否等于 s3 的第 i+j 位（s3[i+j−1]）。
        # 5. 返回 dp[−1][−1]

        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1+len2 != len3:
            return False
        dp = [[False] * (len2+1) for _ in range(len1+1)]
        dp[0][0] = True

        for i in range(1, len1+1):
            dp[i][0] = (dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1, len2+1):
            dp[0][i] = (dp[0][i-1] and s2[i-1]==s3[i-1])

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[len1][len2]

# @lc code=end


#
# @lc app=leetcode id=2707 lang=python
#
# [2707] Extra Characters in a String
#

# @lc code=start
class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        # 设 n 是 s 的长度，现在有两种基本的分割方案：
        # 把 s 的最后一个字符 s[n−1] 当做是额外字符，那么问题转为长度为 n−1 的子问题。
        # 找到一个 j 使得 s 的后缀 s[j...n−1] 构成的子串在 dictionary，那么问题转为长度为 j−1 的子问题
        # 当 i≥1 时，第 i 个字符 s[i−1] 可以作为一个额外字符，此时 f[i]=f[i−1]+1，如果在 j∈[0,i−1] 中存在一个下标 j，使得 s[j..i) 在哈希表 ss 中，那么我们可以将 s[j..i) 作为一个单词，此时 f[i]=f[j]。
        dictset = set(dictionary) 
        n = len(s)
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            for j in range(i):
                if s[j:i] in dictset and dp[j]<dp[i]:
                    dp[i] = dp[j]
        return dp[n]

        @cache
        def dfs(i):
            if i < 0:
                return 0
            res = dfs(i-1) + 1
            for j in range(i+1):
                if s[j:i] in dictset:
                    res = min(res, dfs(j-1))
            return res
        return dfs(len(s) - 1)

# @lc code=end


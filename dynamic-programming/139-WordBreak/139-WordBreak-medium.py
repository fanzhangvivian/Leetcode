#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # complete knapsack problem!!
        # The word is the item, and the string is the backpack. Whether the word can form the string 
        # is equivalent to asking if the item can fill the backpack.
        # When splitting, dictionary words can be used repeatedly, indicating that it is a complete knapsack problem!

        # 1. defination of dp[i]: the length of string is i, and dp[i] is true when it can be splitted into 1or more words
        # 2. recursive formula: if dp[j] is true and [j,i]substring is in the dic then dp[i] is true
        # 3. Initialize: dp[0]=true dp[others] = false( default value is false cuz we dont know the answers)
        # 4. Iterate order: this is a permutation question.

        wordSet = set(wordDict) 
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True 

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]



# @lc code=end


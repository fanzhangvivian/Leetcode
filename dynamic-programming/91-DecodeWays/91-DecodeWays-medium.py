#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return 0 if the string starts with the '0', it is invalid
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # initialize a dp table of (n+1) length
        dp = [0] * (n+1)
        # if the string is empty or just one character, the decode way just has one solution
        dp[0] = 1
        dp[1] = 1

        # iterate the string from the two length
        for i in range(2, n+1):
            # if the one-digit substring is not '0', update dp[i] by adding dp[i - 1] 
            # because we can consider the current digit as a single character.
            # if the two-digit substring is between 10 and 26 (inclusive), update dp[i] by adding dp[i - 2] 
            # because we can consider the current two digits as a single character.
            one_digit = int(s[i-1])
            two_digit = int(s[i-2:i])

            if one_digit != 0:
                dp[i] += dp[i-1]
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        # The final result is stored in dp[n], where n is the length of the input string.
        return dp[n]

# @lc code=end


#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize a dp 2D table to Indicate whether the substring within the interval [i, j] (inclusive on both ends) is a palindromic substring.
        # for each value is False
        # Determine the recurrence formula
        # a.base case:the string of length <= 2: it is a palindrom. Therefore, dp[i][i] = True
        # b.Recursive Case:longer than two characters, a substring s[i:j+1] is a palindrome if and only when s[i]=s[j] and dp[i+1][j-1] is palindrom
        # 3.Iterate the outer loop from the end to the beginning for checking the dp[i+1][j-1]
        # and inner loop from the i to len(s) ensures all possible substrings starting from i are checked.
        # 4. Updating Result and DP Table:Whenever a palindrome is found, update the result counter and mark dp[i][j] as True.
        

        # Initialize the dp 2D table of false result
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        # Interate the back to front for the first order
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j-i <= 1: # 1.first situation:just 2 or 1 character
                        result += 1
                        dp[i][j] = True # mark the current string is true
                    elif dp[i+1][j-1]: #2. more than 2 characters:when we find the substring is Palindromic
                        result += 1
                        dp[i][j] = True
        return result


# @lc code=end


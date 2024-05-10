#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chardict = {}
        for char in s:
            chardict[char] = 1 + chardict.get(char, 0)
        for chart in t:
            if chart in chardict:
                chardict[chart] -= 1
            else:
                chardict[chart] = 1
        for values in chardict.values():
            if values != 0:
                return False
        return True
# @lc code=end


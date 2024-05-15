#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {"(":")", "{":"}", "[":"]"}
        stack = []
        for char in s:
            if char in map:
                stack.append(char)
            elif stack and char == map[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
# @lc code=end


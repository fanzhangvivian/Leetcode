#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # backtracking
        result = []
        left = right = 0
        q = [(left, right, '')]
        while q:
            left, right, s = q.pop()
            if len(s) == 2*n:
                result.append(s)
            if left < n:
                q.append((left+1, right, s + '('))
            if right < left:
                q.append((left, right+1, s + ')'))
        return result
# @lc code=end


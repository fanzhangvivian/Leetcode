#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                digit = stack.pop()
                if char == "+":
                    stack[-1] += digit
                elif char == "-":
                    stack[-1] -= digit
                elif char == "*":
                    stack[-1] *= digit
                else:
                    stack[-1] = int(stack[-1]/digit)
        return stack[0]
# @lc code=end


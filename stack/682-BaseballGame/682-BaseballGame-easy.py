#
# @lc app=leetcode id=682 lang=python
#
# [682] Baseball Game
#

# @lc code=start
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        
        for char in operations:
            if char not in ["C", "D", "+"]:
                stack.append(int(char))
            elif char == "C":
                stack.pop()
            elif char == "D":
                doublenum = stack[-1] * 2
                stack.append(doublenum)
            elif char == "+":
                if len(stack) >= 2:
                    add1 = stack[-1]
                    add2 = stack[-2]
                    add = add1 + add2
                    stack.append(add)
        return sum(stack)

# @lc code=end


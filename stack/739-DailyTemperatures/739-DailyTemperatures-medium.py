#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        # use a stack to record temp index
        # once the current temp > top of stack, we can pop
        # until the top temp > current temp
        # add the smaller current temp into stack
        # use a list of initial value of 0 to update

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(temperatures[i])
        return result
        

# @lc code=end


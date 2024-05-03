#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        result = [0] * len(temperatures) # default a list with len(temp)*0
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()  # pop the index when finding a tem is greater than the index tem
                result[index] = i - index  # record the count by i - index
            stack.append(i) # append the current i into stack to compare

        return result
        

# @lc code=end


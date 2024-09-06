#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key= lambda x:x[0])
        result = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                result += 1
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
        return result
        
# @lc code=end


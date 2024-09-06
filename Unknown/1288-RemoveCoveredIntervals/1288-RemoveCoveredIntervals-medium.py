#
# @lc app=leetcode id=1288 lang=python
#
# [1288] Remove Covered Intervals
#

# @lc code=start
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 按照左端点递增排序， 右端点则是递减
        # 只要满足 左大，右小则可以被覆盖合并

        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, rmax = n, intervals[0][1]
        for i in range(1, n):
            if intervals[i][1] <= rmax:
                ans -= 1
            else:
                rmax = max(rmax, intervals[i][1])
        return ans
# @lc code=end


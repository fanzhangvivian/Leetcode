#
# @lc app=leetcode id=452 lang=python
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort the points with the points[1]
        # if ballons[i] doesn't near ballon[i-1], arow count += 1,
        # else: if they overlap, update minimum right boundary of current ballon, it determine the next ballon will be shot or not
        # initial the arow count 1 when the points length is not 0

        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:
                result += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])

        return result
# @lc code=end


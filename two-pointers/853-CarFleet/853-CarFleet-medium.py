#
# @lc app=leetcode id=853 lang=python
#
# [853] Car Fleet
#

# @lc code=start
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        listtarget_pos = sorted(zip(position, speed))
        timeresult = []
        for p, s in listtarget_pos:
            time = float((target - p) / s)
            timeresult.append(time)
        res = 0
        cur = 0
        for i in timeresult[::-1]:
            if i > cur:
                res += 1
                cur = i
        return res

# @lc code=end


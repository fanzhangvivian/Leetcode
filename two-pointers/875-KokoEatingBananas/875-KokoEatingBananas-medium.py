#
# @lc app=leetcode id=875 lang=python
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        while left < right:
            middlepile = left + (right - left) // 2
            if sum([math.ceil(p/middlepile) for p in piles]) > h:
                left = middlepile + 1
            else:
                right = middlepile
        return left
# @lc code=end


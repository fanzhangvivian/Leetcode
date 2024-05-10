#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        product = [1] * N
        cur = 1
        for i in range(N):
            product[i] = product[i] * cur
            cur = cur * nums[i]
        cur = 1
        for i in range(N-1, -1, -1):
            product[i] = product[i] * cur
            cur = cur * nums[i]
        return product
        
# @lc code=end


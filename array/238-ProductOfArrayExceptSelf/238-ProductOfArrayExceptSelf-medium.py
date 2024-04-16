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
            # Calculate the left product of index i
            product[i] = product[i] * cur
            cur = cur * nums[i]
        cur = 1
        for i in range(N-1, -1, -1):
            # Calculate the right product of index i in reverse order
            # Note that it should start from the last position.
            product[i] = product[i] * cur
            cur = cur * nums[i]

        return product

        
# @lc code=end


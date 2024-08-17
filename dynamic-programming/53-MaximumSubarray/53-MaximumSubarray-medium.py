#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count  # Update the result if the current subarray sum is greater
            if count < 0:   # it means recent count is negative no contribute to the result
                count = 0  # reset the count to search 
        return result



# @lc code=end


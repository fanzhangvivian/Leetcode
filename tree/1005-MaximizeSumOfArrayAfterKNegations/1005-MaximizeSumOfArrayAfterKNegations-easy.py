#
# @lc app=leetcode id=1005 lang=python
#
# [1005] Maximize Sum Of Array After K Negations
#

# @lc code=start
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 1.negative int: find the maximum absolute value and turn it to -nums[i]
        # 2.positive int: find the minimum value and turn it to -nums[i]

        nums.sort(key = lambda x:abs(x), reverse= True) # sort it by absolute value 
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        if k % 2 == 1:
            nums[-1] *= -1
        result = sum(nums)
        return result
        
            
            
# @lc code=end


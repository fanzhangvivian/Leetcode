#
# @lc app=leetcode id=674 lang=python
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # similar to question 300
        # Defination: dp[i]:the length of the longest continuous increasing subsequence that ends at index i and includes nums[i]
        # Recursive Formula: just need to compare the nums[i-1] and nums[i]
        # if nums[i]>nums[i-1]: dp[i] = dp[i-1] + 1
        # Initialize dp[1] = 1
        # Iterate order: from beginning to end

        n = len(nums)
        if n == 0:
            return 0
        result = 1
        dp = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            result = max(result, dp[i])
        return result
# @lc code=end


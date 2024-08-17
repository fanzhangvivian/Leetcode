#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Defination： dp[i]:the length of the longest increasing subsequence that ends at index i and includes nums[i]
        # If nums[i] is greater than nums[j], update dp[i] to the maximum value between dp[i] and dp[j] + 1
        
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        result = 1
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

            result = max(result, dp[i])
            
        return result

# @lc code=end


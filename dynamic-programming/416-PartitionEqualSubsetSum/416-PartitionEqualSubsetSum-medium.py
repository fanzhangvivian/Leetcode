#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 01 bag Question
        # dp[j]: maximum value of j bag
        # weight = value, dp[target] == target
        # dp[j] = max(dp[j], dp[j-nums[i]]+nums[j]): maxmium value of (put item i and don't put item i)
        # Initialize the dp[0] = 0

        total_sum = sum(nums) 

        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2

        dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # 初始化第一行（空子集可以得到和为0）
        for i in range(len(nums)+1):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, target_sum + 1):
                # when current num>target sum, we should skip
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]])
        
        return dp[len(nums)][target_sum]
# @lc code=end


#
# @lc app=leetcode id=377 lang=python
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # dp[][j]和为j的组合的总数
        dp = [[0] * (target+1) for _ in nums]

        for i in range(len(nums)):
            dp[i][0] = 1
        
        for j in range(1, target+1):
            for i in range(len(nums)):
                if j-nums[i] >= 0:
                    # 不放nums[i] i = 0 时，dp[-1][j]恰好为0，所以没有特殊处理
                    dp[i][j] = (dp[i-1][j] 
                    # 放nums[i]。对于和为j的组合，只有试过全部物品，才能知道有几种组合方式。所以取最后一个物品dp[-1][j-nums[i]]
                    + dp[-1][j-nums[i]]
                    ) 
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
# @lc code=end


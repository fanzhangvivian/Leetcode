#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # seperate it into 2 situation 1:exclude the last one 2:exclude the first one
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])

        def houseRobber(nums):
            dp = [0] * len(nums)

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                # for each room, the biggest amount of money that can be robbed is between the last 2 rooms
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])

            # return the last room's amount money
            return dp[-1] 

        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))
# @lc code=end


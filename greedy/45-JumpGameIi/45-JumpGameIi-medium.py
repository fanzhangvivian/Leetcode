#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 每一步尽可能增加覆盖范围，用最少的步数增加覆盖范围
        # each step record the maximum cover rage
        
        if len(nums) <= 1:
            return 0
        curCover = 0 # 当前覆盖的距离
        nextCover = 0 # 下一次覆盖的距离
        result = 0

        for i in range(len(nums)):
            nextCover = max(i + nums[i], nextCover)
            if i == curCover and curCover != len(nums) - 1: # 已经跳到当前覆盖范围，但不是终点位置
                result += 1
                curCover = nextCover  # 更新当前覆盖最远距离下标（相当于加油了）
                if nextCover >= len(nums) - 1:
                    break
        
        return result
# @lc code=end


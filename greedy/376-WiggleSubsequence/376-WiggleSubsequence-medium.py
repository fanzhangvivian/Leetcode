#
# @lc app=leetcode id=376 lang=python
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        curDiff = 0  # 当前一对元素的差值
        preDiff = 0   # 前一对元素的差值
        result = 1  # 记录峰值的个数，初始为1（默认最右边的元素被视为峰值

        for i in range(len(nums)-1):
            curDiff = nums[i+1] - nums[i]  # 计算下一个元素与当前元素差值
            # 如果遇到一个峰值
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1  # 峰值个数+1
                preDiff = curDiff  # 只有在摆动的时候，更新preDiff
        return result
# @lc code=end


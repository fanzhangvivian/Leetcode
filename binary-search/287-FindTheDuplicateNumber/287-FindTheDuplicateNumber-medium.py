#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the duplicate number between 1 to n 
        low, high = 1, len(nums)-1
        while low < high:
            mid = (low + high) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            # n + 1 个整数，放在长度为 n 的数组里，根据「抽屉原理」，
            # 至少会有 1 个整数是重复的；
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low
# @lc code=end


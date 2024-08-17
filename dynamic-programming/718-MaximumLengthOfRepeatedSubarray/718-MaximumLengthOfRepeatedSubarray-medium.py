#
# @lc app=leetcode id=718 lang=python
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # d[i][j]: 2D array:the maximum length of subarray ending at index[i-1] of numbers1 array and index[j-1] of numbers2 array 以i-1结尾的数组1和以j-1结尾的数组2
        # dp【i】【j】是以i-1与j-1号元素作为结尾的公共子数组的长度. 即 公共子数组的结尾必须是i-1和j-1, 
        # 所以,当i-1 != j-1 时, dp【i】【j】=0, 如果相同 dp【i】【j】 = dp【i-1】【j-1】+1
        
        # Create a 2d Array
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        result = 0

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                # if nums[i-1] == nums[j-1] we can continue iterate and add 1 to current length
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # update the maximum length of subarray
                if dp[i][j] > result:
                    result = dp[i][j]
        return result
        
# @lc code=end


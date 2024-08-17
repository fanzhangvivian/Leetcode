#
# @lc app=leetcode id=1035 lang=python
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # the same solve solution logic with 1143 question
        # to find the longest commen subarray 

        dp = [([0] * (len(nums2) + 1)) for _ in range(len(nums1) + 1)]

        result = 0

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                elif nums1[i-1] != nums2[j-1]:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                if dp[i][j] > result:
                    result = dp[i][j]

        return result
# @lc code=end 


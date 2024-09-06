#
# @lc app=leetcode id=763 lang=python
#
# [763] Partition Labels
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # bulletpoint: 找出每个元素的最长出现距离下标，记录当前元素里最长的下标距离，当index 与最长距离下标一致时，则可以分割一个区间

        last_consequence = {}
        for i, con in enumerate(s):
            last_consequence[con] = i

        result = []
        start = 0
        end = 0
        for i, con in enumerate(s):
            end = max(end, last_consequence[con])
            if i == end:  # 说明当前的index是前面所有元素里下标最长的距离
                result.append(end-start+1)
                start = i+1
        return result
# @lc code=end


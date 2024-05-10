#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        charset = set()
        for char in nums:
            if char in charset:
                return True
            charset.add(char)
        return False
# @lc code=end


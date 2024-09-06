#
# @lc app=leetcode id=1899 lang=python
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # 在三个元素都小于target的三元组里，取最大值

        x, y, z = target
        a, b, c = 0, 0, 0
        for ai, bi, ci in triplets:
            if ai <= x and bi <= y and ci <= z:
                a, b, c = max(a, ai), max(b, bi), max(c, ci)
        
        return (a, b, c) == (x, y, z)
# @lc code=end


#
# @lc app=leetcode id=455 lang=python
#
# [455] Assign Cookies
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 局部最优->全局最优 且找不出反例，则用贪心
        # 大饼干满足大胃口小朋友
        # use the max cookies to content the child with greed factor
        # iterate from back to end
        g.sort() #sort from small to big
        s.sort()
        index = len(s) - 1 # cookies' last index
        result = 0
        for i in range(len(g)-1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                result += 1
                index -= 1
        return result

# @lc code=end


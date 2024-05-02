#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        count1, count2 = Counter(s1), Counter(s2[:n1])
        for i in range(n1, n2):
            if count1 == count2:
                return True
            count2[s2[i-n1]] -= 1 # slide the left
            count2[s2[i]] += 1 # slide the right
        return count1 == count2
        
# @lc code=end


#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        left = 0
        maxlen = 0
        strset = set()
        for right in range(len(s)):
            # Slide the right pointer to record the max length
            if s[right] not in strset:
                strset.add(s[right])
                maxlen = max(maxlen, len(strset))
            else:
                # Slide the left pointer until the repeated charcater dont occur
                # Remove all characters preceding the repeated character and itself from the current window
                while s[right] in strset:
                    strset.remove(s[left])
                    left += 1 # Slide the left pointer to adjust the window.
                strset.add(s[right]) # Add the current character to the window set.
        return maxlen
        
# @lc code=end


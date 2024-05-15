#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Bullet point: 1.find the valid window;
        # 2. how to find valid window that the window length subtract the most frequency is less or equal to k
        # 3. Always keep the longest window length until find the longer window.
        left = 0
        frequency = {}
        maxlength = float('-inf')
        for right in range(len(s)):
            frequency[s[right]] = 1 + frequency.get(s[right], 0)
            current_window_length = right - left + 1
            current_max_frequency = max(frequency.values())
            if current_window_length - current_max_frequency <= k:
                maxlength = max(maxlength, current_window_length)
            else:
                frequency[s[left]] -= 1
                left += 1
        return maxlength
        
# @lc code=end


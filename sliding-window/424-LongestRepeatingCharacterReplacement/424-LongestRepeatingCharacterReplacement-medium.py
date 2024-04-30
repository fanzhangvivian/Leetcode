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
        # Slide the valid replace window
        # Bullet point: how to find the valid window
        # 1. Find the most frequency in the window
        # 2. Use the current window length subscribe the most frequency number;
        # 3. If it is smaller and equal to k, it indicates that it is a valid window;
        # since the replacement number is smaller and equal to k. 
        # right pointer continue slide for longer window. Also update the current max length of the window
        # 4. If it is bigger than k, it indicates that it is a unvalid window 
        # since the replacement number is bigger 
        # Then slide the left pointer to ensure the window is valid. In the meanwhile,
        # the frequency of the left pointer should reduce 1
        countfrequency = {}
        left = 0
        maxlen = 0
        for right in range(len(s)):
            if s[right] in countfrequency:
                countfrequency[s[right]] += 1
            else:
                countfrequency[s[right]] = 1
            current_window_len = right - left + 1 # the current window length
            current_max_frequency = max(countfrequency.values()) # Find the most frequency in the window
            if current_window_len - current_max_frequency <= k:
                maxlen = max(maxlen, current_window_len) # update the current max length of the valid window
            else:
                countfrequency[s[left]] -= 1
                left += 1  # slide the left pointer to ensure the window is valid
        return maxlen
        
# @lc code=end


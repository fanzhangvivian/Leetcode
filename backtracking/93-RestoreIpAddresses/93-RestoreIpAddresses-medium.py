#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.backtracking(s, 0, 0, "", result)
        return result
    
    def backtracking(self, s, startindex, point_sum, current, result):
        if point_sum == 3: # decide the deepth of backtracking
            if self.isvalid(s, startindex, len(s)-1):
                current += s[startindex:]
                result.append(current)
            return
        for i in range(startindex, len(s)):
            if self.isvalid(s, startindex, i):
                sub = s[startindex:i + 1]
                self.backtracking(s, i+1, point_sum + 1, current + sub + ".", result)
            else:
                break
                
    def isvalid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:
            return False
        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
            num = num * 10 + int(s[i])
            if num > 255:
                return False
        return True
        
# @lc code=end


#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.backtracking(s, 0, [], result)
        return result
    
    def backtracking(self, s, startindex, path, result):
        if startindex == len(s):
            result.append(path[:])
            return
        
        for i in range(startindex, len(s)):
            if self.is_palindrome(s, startindex, i):
                path.append(s[startindex: i+1])
                self.backtracking(s, i+1, path, result)
                path.pop()

    def is_palindrome(self, s, start, end):
        i = start
        j = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
# @lc code=end


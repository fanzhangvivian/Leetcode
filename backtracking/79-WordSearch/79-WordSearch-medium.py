#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # terminal case: if out of boundary or not match: return False
        # if the index == len(word) - 1,return true
        # iterate 4 direction to search and record the index 
        # visit:marked as "*" 
        # after searching, reset the vistied into initial
        def backtracking(i, j, index):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            board[i][j] = "*"
            res = False
            for m, n in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + m, j+n
                if backtracking(ni, nj, index + 1):
                    res = True
                    break
            board[i][j] = word[index]
            return res
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(i, j, 0):
                    return True

        return False
# @lc code=end


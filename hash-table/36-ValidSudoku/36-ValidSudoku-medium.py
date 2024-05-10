#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
import collections
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sudokumap = collections.defaultdict(list)
        for x in range(len(board)):
            for y in range(len(board)):
                char = board[x][y]
                if char != ".":
                    if char in sudokumap:
                        for position in sudokumap[char]:
                            if position[0] == x or position[1] == y or (position[0]//3 == x//3 and position[1]//3== y//3):
                                return False
                    sudokumap[char].append((x, y))
        return True

                
        
# @lc code=end


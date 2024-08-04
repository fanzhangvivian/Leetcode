#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def capture(i, j):
            if i < 0 or j < 0 or i == rows or j == cols or board[i][j] != "O":
                return 
            board[i][j] = "B"
            capture(i+1, j)
            capture(i-1, j)
            capture(i, j+1)
            capture(i, j-1)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row in (0, rows-1) or col in (0, cols-1)):
                    capture(row, col)
            
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "B":
                    board[row][col] = "O"

# @lc code=end


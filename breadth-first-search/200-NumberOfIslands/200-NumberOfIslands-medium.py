#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
import collections
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    grid[row][col] = '0'

                    land_positions = collections.deque()
                    land_positions.append([row, col])
                    while len(land_positions) > 0:
                        x, y = land_positions.popleft()
                        for new_x, new_y in [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]:
                            if 0 <= new_x < len(grid) and 0<= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'
                                land_positions.append([new_x, new_y])
        return count
# @lc code=end


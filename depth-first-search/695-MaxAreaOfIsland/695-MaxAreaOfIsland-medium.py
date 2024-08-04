#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS 
        # 
        m, n = len(grid), len(grid[0])
        def bfs(i, j):
            queue = [(i, j)]
            grid[i][j] = 0
            area = 1
            while queue:
                x, y = queue.pop()
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                        grid[nx][ny] = 0
                        area += 1
                        queue.append((nx, ny))
            return area
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, bfs(i, j))
        return res



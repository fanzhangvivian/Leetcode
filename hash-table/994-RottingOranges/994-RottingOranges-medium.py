#
# @lc app=leetcode id=994 lang=python
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 1. Using a list to record the initial rotting oranges's location and intialize fresh oranges' number
        # 2. Using bfs to get each level's rotting oranges' 4-directionally adjacent fresh oranges
        # and convert the fresh oranges into rotting oranges and then add them into this level's rotting oranges 
        # 3. return -1 if fresh is still > 0 or return maxmium of ans and 0
        m, n = len(grid), len(grid[0])
        fresh = 0
        rotting = []
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    fresh += 1  
                elif col == 2:
                    rotting.append((i, j))  # 一开始就腐烂的橘子

        ans = -1
        while rotting:
            ans += 1  # 经过一分钟
            tmprotting = rotting
            rotting = []
            for x, y in tmprotting:  # 已经腐烂的橘子
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):  # 四方向
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:  # 新鲜橘子
                        fresh -= 1
                        grid[i][j] = 2  # 变成腐烂橘子
                        rotting.append((i, j))

        return -1 if fresh else max(ans, 0)


# @lc code=end


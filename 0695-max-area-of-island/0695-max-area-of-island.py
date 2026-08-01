class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(x, y):
            if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                grid[x][y] = 0

                return 1+dfs(x+1,y)+dfs(x-1,y)+dfs(x,y+1)+dfs(x,y-1)

            return 0

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))

        return res
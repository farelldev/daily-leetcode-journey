class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def dfs(x, y):
            grid[y][x] = '0'

            if y < len(grid) - 1 and grid[y+1][x] == '1':
                dfs(x, y+1)
            if y != 0 and grid[y-1][x] == '1':
                dfs(x, y-1)
            if x < len(grid[y]) - 1 and grid[y][x+1] == '1':
                dfs(x+1, y)
            if x != 0 and grid[y][x-1] == '1':
                dfs(x-1, y)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(j, i)

        return ans
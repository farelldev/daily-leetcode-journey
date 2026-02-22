class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def dfs(x, y):
            outX = x < 0 or x > len(grid[0]) - 1
            outY = y < 0 or y > len(grid) - 1
            outBound = outX or outY

            if outBound or grid[y][x] == '0':
                return

            grid[y][x] = '0'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(j, i)

        return ans
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        seen = [[False for _ in range(col)] for _ in range(row)]
        res = 0

        def bfs(x, y):
            if x == len(grid) or y == len(grid[0]) or x == -1 or y == -1 or seen[x][y] == True or grid[x][y] == '0':
                return

            seen[x][y] = True
            bfs(x, y + 1)
            bfs(x + 1, y)
            bfs(x, y - 1)
            bfs(x - 1, y)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and seen[i][j] == False:
                    bfs(i, j)
                    res += 1
                    print(i, j)

        print(seen)
        return res
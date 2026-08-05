class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        canPac = [[False for _ in range(col)] for _ in range(row)]
        canAtl = [[False for _ in range(col)] for _ in range(row)]
        res = []
        
        def dfs(i, j, ocean):
            if 0 <= i < row and 0 <= j < col and not ocean[i][j]:
                ocean[i][j] = True

                for dx, dy in dirs:
                    adjX = i + dx
                    adjY = j + dy
                    if 0 <= adjX < row and 0 <= adjY < col and heights[i][j] <= heights[adjX][adjY]:
                        dfs(adjX, adjY, ocean)

        for i in range(row):
            dfs(i, 0, canPac)
            dfs(i, col - 1, canAtl)

        for j in range(col):
            dfs(0, j, canPac)
            dfs(row - 1, j, canAtl)

        for i in range(row):
            for j in range(col):
                if canPac[i][j] and canAtl[i][j]:
                    res.append([i, j])

        return res
        
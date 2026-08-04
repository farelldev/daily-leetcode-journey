class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        row = len(grid)
        col = len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        q = deque()
        res = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))

        while q:
            manyRot = len(q)
            rotting = False

            for _ in range(manyRot):
                curRot = q.popleft()

                for dx, dy in dirs:
                    adj = (curRot[0] + dx, curRot[1] + dy)

                    if 0 <= adj[0] < row and 0 <= adj[1] < col and grid[adj[0]][adj[1]] == 1:
                        grid[adj[0]][adj[1]] = 2
                        q.append(adj)
                        rotting = True

            if rotting: res += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = -1

        return res
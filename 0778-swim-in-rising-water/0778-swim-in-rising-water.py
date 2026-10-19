class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        visited = set()
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for t in range(n * n):
            if grid[0][0] <= t:
                visited.add((0, 0))

            if (0, 0) not in visited:
                continue

            while True:
                added = False

                for i, j in list(visited):
                    for x, y in dirs:
                        ni, nj = i + x, j + y

                        if 0 <= ni < n and 0 <= nj < n:
                            if (ni, nj) not in visited and grid[ni][nj] <= t:
                                visited.add((ni, nj))
                                added = True

                if not added:
                    break

            if (n - 1, n - 1) in visited:
                return t

        return -1
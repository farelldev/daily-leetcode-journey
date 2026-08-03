class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        captured = [[True for _ in range(col)] for _ in range(row)]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(x, y):
            if 0 <= x < row and 0 <= y < col and captured[x][y] and board[x][y] == 'O':
                captured[x][y] = False

                for dx, dy in dirs:
                    dfs(x + dx, y + dy)

        for i in range(row):
            if board[i][0] == 'O' and captured[i][0]:
                dfs(i, 0)
            if board[i][col - 1] == 'O' and captured[i][col - 1]: 
                dfs(i, col - 1)

            print([i, 0], [i, col - 1])

        for i in range(col):
            if board[0][i] == 'O' and captured[0][i]: 
                dfs(0, i)
            if board[row - 1][i] == 'O' and captured[row - 1][i]:
                dfs(row - 1, i)
                
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and captured[i][j]:
                    board[i][j] = 'X'
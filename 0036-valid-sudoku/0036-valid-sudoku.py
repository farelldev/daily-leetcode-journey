class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i : set() for i in range(9)}
        cols = {i : set() for i in range(9)}
        subs = {i : set() for i in range(9)}

        for row in range(9):
            for col in range(9):
                grid = board[row][col]

                rowSub = (row) // 3
                colSub = (col) // 3
                boxSub = 3 * rowSub + colSub

                if grid in rows[row] or grid in cols[col] or grid in subs[boxSub]:
                        return False
                elif grid != ".":
                    rows[row].add(grid)
                    cols[col].add(grid)
                    subs[boxSub].add(grid)

        return True
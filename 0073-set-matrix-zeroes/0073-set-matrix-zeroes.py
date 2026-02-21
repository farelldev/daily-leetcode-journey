class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = set()
        row = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in col:
            for j in range(len(matrix)):
                matrix[j][i] = 0

        for j in row:
            for i in range(len(matrix[j])):
                matrix[j][i] = 0
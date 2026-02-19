class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        find = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    find.append([i,j])

        for coor in find:
            for row in range(len(matrix)):
                matrix[row][coor[1]] = 0
            for col in range(len(matrix[0])):
                matrix[coor[0]][col] = 0
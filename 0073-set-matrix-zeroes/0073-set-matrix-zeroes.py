class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        random = 948320283

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: matrix[i][j] = random

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == random:
                    matrix[i][j] = 0

                    # left
                    for k in range(j - 1, -1, -1):
                        matrix[i][k] = 0 if matrix[i][k] != random else random
                    # right
                    for k in range(j + 1, len(matrix[0])):
                        matrix[i][k] = 0 if matrix[i][k] != random else random
                    # up
                    for k in range(i - 1, -1, -1):
                        matrix[k][j] = 0 if matrix[k][j] != random else random
                    # down
                    for k in range(i + 1, len(matrix)):
                        matrix[k][j] = 0 if matrix[k][j] != random else random
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1

        while l <= r or t <= b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            if b == t: break

            for i in range(t+1, b + 1):
                res.append(matrix[i][r])
            if r == l: break

            for i in range(r-1, l-1, -1):
                res.append(matrix[b][i])
            if b == t+1: break

            for i in range(b-1, t, -1):
                res.append(matrix[i][l])
            if r == l+1: break

            l += 1
            r -= 1
            t += 1
            b -= 1

        return res
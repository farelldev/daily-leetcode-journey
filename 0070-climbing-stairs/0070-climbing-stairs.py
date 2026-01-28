class Solution:
    def climbStairs(self, n: int) -> int:
        res = []

        for i in range(n):
            if i <= 1: res.append(i+1)
            else: res.append(res[i-1] + res[i-2])

        return res[n-1]
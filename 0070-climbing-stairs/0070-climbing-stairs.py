class Solution:
    def climbStairs(self, n: int) -> int:
        first = 2
        second = 3

        if 1 <= n <= 3: return n

        for i in range(3, n):
            first, second = second, first + second

        return second
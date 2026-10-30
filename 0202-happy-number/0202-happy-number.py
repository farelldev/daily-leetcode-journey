class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            curr = []
            while n > 0:
                digit = n % 10
                curr.append(digit**2)
                n = n // 10
            square = sum(curr)
            n = square
            if square == 1: return True
            if square in visited: return False
            visited.add(square)
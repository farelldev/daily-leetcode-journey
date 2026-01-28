class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        
        one, two = 2, 1
        for i in range(2, n):
            curr = one + two
            one, two = curr, one
            
        return curr
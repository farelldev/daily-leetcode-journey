class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = list(bin(n))

        for i in range(len(s)):
            if i != 0 and s[i] == s[i-1]:
                return False

        return True
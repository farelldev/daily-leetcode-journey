class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if 0 <= len(s) <= 1: return len(s)
        
        res = l = 0
        for r in range(1, len(s) + 1):
            res = max(res, len(set(s[l:r])))

            if r == len(s): break
            while s[r] in set(s[l:r]):
                l += 1

        return res
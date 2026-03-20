class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        res = l = maxf = 0

        for r in range(len(s)):
            cnt[s[r]] = 1 + cnt.get(s[r], 0)
            maxf = max(maxf, cnt[s[r]])

            while (r - l + 1) - maxf > k:
                cnt[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
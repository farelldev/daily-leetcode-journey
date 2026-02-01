class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        
        for a in range(len(text1) - 1, -1, -1):
            for b in range(len(text2) - 1, -1, -1):
                if text1[a] == text2[b]:
                    dp[a][b] = 1 + dp[a + 1][b + 1]
                else:
                    dp[a][b] = max(dp[a][b + 1], dp[a + 1][b])

        return dp[0][0]
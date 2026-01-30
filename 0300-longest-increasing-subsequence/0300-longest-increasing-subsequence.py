class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for sub in range(i):
                if nums[sub] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[sub])

        return max(dp)
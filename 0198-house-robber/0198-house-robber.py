class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums.copy()

        for i in range(2, len(nums)):
            for j in range(i - 1):
                dp[i] = max(dp[i], nums[i] + dp[j])

        return max(dp)
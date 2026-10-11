class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        n = len(nums)

        for i in range(n):
            if farthest >= n - 1: return True
            if i > farthest: return False

            if i + nums[i] > farthest:
                farthest = i + nums[i]
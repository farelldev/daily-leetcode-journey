class Solution:
    def jump(self, nums: list[int]) -> int:
        farthest = res = lastJump = 0
        n = len(nums)

        if 0 <= n <= 1: return 0

        for i in range(n):
            if farthest < i + nums[i]:
                farthest = i + nums[i]

            if i == lastJump:
                lastJump = farthest
                res += 1
                
                if farthest >= n - 1: return res
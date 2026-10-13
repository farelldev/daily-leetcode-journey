class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3: return max(nums)

        for i in range(len(nums) - 3, -1, -1):
            if i == len(nums) - 3:
                nums[i] += nums[i+2]
            else:
                nums[i] = max(nums[i] + nums[i+3], nums[i] + nums[i+2])

        return max(nums[0], nums[1])
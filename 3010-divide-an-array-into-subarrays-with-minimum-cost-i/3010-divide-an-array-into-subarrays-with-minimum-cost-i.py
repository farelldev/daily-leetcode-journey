class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1 = min2 = float('inf')

        for i in range(1, len(nums)):
            if nums[i] < min1:
                min1 = nums[i]
                idx = i

        for i in range(1, len(nums)):
            if nums[i] < min2 and idx != i:
                min2 = nums[i]

        return nums[0] + min1 + min2
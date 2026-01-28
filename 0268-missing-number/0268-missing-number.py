class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(None)

        for i in range(len(nums)):
            if i != nums[i]: return i
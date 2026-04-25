class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashT = {}

        for i in range(len(nums)):
            if target - nums[i] in hashT:
                return [hashT[target - nums[i]], i]

            hashT[nums[i]] = i
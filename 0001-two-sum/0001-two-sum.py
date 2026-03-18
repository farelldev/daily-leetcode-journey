class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}

        for i, val in enumerate(nums):
            if (target - val) in hset:
                return hset[target - val], i
            
            hset[val] = i
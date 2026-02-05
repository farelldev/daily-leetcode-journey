class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            pos = (i + nums[i]) % len(nums)
            res.append(nums[pos])
            
        return res
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = curr = 0

        for i in nums:
            if i == 1: 
                curr+=1
            else: curr = 0
            res = max(curr, res)

        return res
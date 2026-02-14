class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        unik = set(nums)
        dobel = 0
        for num in nums:
            dobel ^= num
        for num in unik:
            dobel ^= num
            
        for i in range(len(nums)):
            if i+1 not in unik:
                return [dobel, i+1]
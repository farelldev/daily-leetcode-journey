class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i, yes = 0, False
        p = q = False
        
        while i < len(nums) - 1 and nums[i+1] > nums[i]:
            i += 1
            p = True
        while p and i < len(nums) - 1 and nums[i+1] < nums[i]:
            i += 1
            q = True
        while q and i < len(nums) - 1 and nums[i+1] > nums[i]:
            i += 1
            yes = True

        return yes and i == len(nums) - 1
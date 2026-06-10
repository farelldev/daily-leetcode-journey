class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        
        while i < len(nums):
            if i == 0 or nums[i] != nums[i-1]:
                k += 1
                i += 1
            else:
                while nums[i] == nums[i-1]:
                    nums.remove(nums[i])

                    if i == len(nums): break

        return k
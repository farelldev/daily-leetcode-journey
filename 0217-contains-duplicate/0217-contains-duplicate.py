class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        curr = None
        for num in sorted(nums):
            if curr == num: return True
            curr = num
        return False
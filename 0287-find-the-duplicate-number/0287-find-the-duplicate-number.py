class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        clean = set()

        for i in nums:
            if i not in clean: clean.add(i)
            else: return i
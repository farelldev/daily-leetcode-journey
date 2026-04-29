class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        unique = set(nums)
        res = 1

        for num in unique:
            if num - 1 not in unique:
                curr = 1
                cons = num

                while cons + 1 in unique:
                    cons += 1
                    curr += 1
                    res = max(res, curr)

        return res
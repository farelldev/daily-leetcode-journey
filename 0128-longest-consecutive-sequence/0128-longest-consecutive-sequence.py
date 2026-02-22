class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        maxi = 0

        for i in uniq:
            if i - 1 not in uniq:
                curr = 0
                while i + curr in uniq:
                    curr += 1
                maxi = max(curr, maxi)
        return maxi
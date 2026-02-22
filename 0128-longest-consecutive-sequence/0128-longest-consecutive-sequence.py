class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        maxi = curr = 1

        if not nums: return 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                curr = 1
            maxi = max(maxi, curr)

        return maxi
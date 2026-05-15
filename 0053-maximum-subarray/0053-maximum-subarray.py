class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = r = curr = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            r = i
            curr += nums[i]

            while (nums[l] < 0 or curr < 0) and l < r:
                curr -= nums[l]
                l += 1

            maxSum = max(curr, maxSum)
        
        return maxSum
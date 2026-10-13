class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 3: return max(nums)

        nums1 = nums[:-1]
        nums2 = nums[1:]
        n = len(nums1)

        if n == 3: 
            res1 = max(nums1[0] + nums1[2], nums1[1])
            res2 = max(nums2[0] + nums2[2], nums2[1])
            return max(res1, res2) 

        for i in range(n - 3, -1, -1):
            if i == n - 3:
                nums1[i] += nums1[i + 2]
                nums2[i] += nums2[i + 2]
            else:
                nums1[i] += max(nums1[i + 2], nums1[i + 3])
                nums2[i] += max(nums2[i + 2], nums2[i + 3])

        return max(nums1[0], nums1[1], nums2[0], nums2[1])
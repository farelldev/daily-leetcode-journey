class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        order = {}

        order[1] = nums[len(nums) - 1]
        cnt = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                for j in range(1, cnt + 1):
                    if nums[i] > order[j]:
                        order[j] = nums[i]
                        break
                    if nums[i] == order[j]: break
                else:
                    cnt += 1
                    order[cnt] = nums[i]

        return cnt
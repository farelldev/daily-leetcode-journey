class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1, l2 = nums[:n], nums[n:]
        p = 0
        ans = []

        for i in range(n):
            ans.append(l1[i])
            ans.append(l2[i])

        return ans
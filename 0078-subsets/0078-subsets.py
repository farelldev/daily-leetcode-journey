class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def createSubset(i, subset):
            if i == len(nums):
                res.append(copy.copy(subset))
                return

            subset.append(nums[i])
            createSubset(i + 1, subset)
            subset.pop()
            createSubset(i + 1, subset)

        res = []
        createSubset(0, [])
        return res
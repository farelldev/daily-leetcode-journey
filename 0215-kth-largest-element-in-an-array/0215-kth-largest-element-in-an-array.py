class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)

        for i in nums:
            heapq.heappush(h, i)

            if len(h) > k:
                heapq.heappop(h)

        return h[0]
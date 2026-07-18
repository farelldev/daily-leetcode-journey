class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxH = [-x for x in stones]
        heapq.heapify(maxH)

        while len(maxH) > 1:
            x = heapq.heappop(maxH)
            y = heapq.heappop(maxH)

            if x != y:
                heapq.heappush(maxH, -abs(x-y))
        
        if maxH: return abs(maxH[0])
        return 0
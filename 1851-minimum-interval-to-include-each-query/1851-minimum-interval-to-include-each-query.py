class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals = sorted(intervals)[::-1]
        h = []
        res = {}
        for q in sorted(queries):
            while intervals and intervals[-1][0] <= q:
                i, j = intervals.pop()
                if j >= q:
                    heapq.heappush(h, [j - i + 1, j])
            while h and h[0][1] < q:
                heapq.heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]
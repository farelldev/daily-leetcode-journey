class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        from collections import defaultdict

        frontier = [(0, k)]
        visit = set()
        neig = defaultdict(list)
        res = 0

        for time in times:
            neig[time[0]].append((time[1], time[2]))

        while frontier:
            curr = heapq.heappop(frontier)
            if curr[1] in visit: continue
            
            visit.add(curr[1])
            res = curr[0]

            for i in neig[curr[1]]:
                if i[0] not in visit:
                    heapq.heappush(frontier, (curr[0] + i[1], i[0]))

        if len(visit) != n: res = -1
        return res
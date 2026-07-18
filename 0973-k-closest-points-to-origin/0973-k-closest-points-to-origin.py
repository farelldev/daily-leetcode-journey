class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cntDistance(x, y):
            return sqrt(x ** 2 + y ** 2)

        h = []
        heapq.heapify(h)

        for i in points: 
            heapq.heappush(h, (-cntDistance(i[0], i[1]), i))

            if len(h) > k: heapq.heappop(h)

        res = []
        for i in h:
            res.append(i[1])
        
        return res
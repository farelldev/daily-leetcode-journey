class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cntDistance(x, y):
            return sqrt(x ** 2 + y ** 2)

        dPair = [(i, cntDistance(i[0], i[1])) for i in points]

        d = [i[1] for i in dPair]

        d.sort()

        res = []
        for i in dPair:
            if i[1] <= d[k - 1]: res.append(i[0])

        return res
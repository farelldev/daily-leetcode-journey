class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            curr = intervals[i]

            if newInterval[1] < curr[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > curr[1]:
                res.append(curr)
            else:
                newInterval = [min(curr[0], newInterval[0]), max(curr[1], newInterval[1])]

        res.append(newInterval)
        return res
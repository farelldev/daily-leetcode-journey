class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # If newIn behind interval
                res.append(newInterval) # Append the newIn
                return res + intervals[i:]  # Return it right away

            elif newInterval[0] > intervals[i][1]: # If interval behind newIn 
                res.append(intervals[i])    # Append that interval

            else: # If overlapping
                # Extend newInterval
                newInterval = [min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])]

        # Append newInterval at the end
        res.append(newInterval)

        return res
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        self.leng = 0

        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        self.leng += 1

        if len(self.large) > len(self.small):
            if num < self.large[0]:
                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(self.large, num)
                heapq.heappush(self.small, -heapq.heappop(self.large))

        elif len(self.large) < len(self.small):
            if -num < self.small[0]:
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(self.small, -num)
                heapq.heappush(self.large, -heapq.heappop(self.small))

        else:
            if self.small and -num > self.small[0]:
                heapq.heappush(self.small, -num)
            else: heapq.heappush(self.large, num)

    def findMedian(self) -> float:
        if self.leng % 2 != 0: 
            if len(self.large) > len(self.small):
                return self.large[0]
            else: return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.length += 1

    def findMedian(self) -> float:
        self.nums.sort()
        mid = self.length // 2
        median = float(self.nums[mid]) if self.length % 2 == 1 else (self.nums[mid] + self.nums[mid - 1]) / 2

        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
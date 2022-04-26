from heapq import heappush, heappop
class MedianFinder:
    # minheap by default
    def __init__(self):
        self.min = [] # upper half
        self.max = [] # lower half

    def addNum(self, num: int) -> None:
        if len(self.min) >= len(self.max):
            heappush(self.min, num)
            # print(">=", self.max, self.min)
            heappush(self.max, -(heappop(self.min)))
            # print(">=", self.max, self.min)
        else:
            heappush(self.max, -num)
            # print("<", self.max, self.min)
            heappush(self.min, -(heappop(self.max)))
            # print("<", self.max, self.min)

    def findMedian(self) -> float:
        # print(self.max, self.min)
        if len(self.min) > len(self.max):
            return self.min[0]
        elif len(self.min) < len(self.max):
            return -self.max[0]
        else:
            return (-self.max[0] + self.min[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
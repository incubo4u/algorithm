from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, -num)
        while abs(len(self.maxheap) - len(self.minheap)) > 1 or (
            (self.maxheap and self.minheap) and -self.maxheap[0] > self.minheap[0]
        ):
            if len(self.maxheap) > len(self.minheap) or (
                (self.maxheap and self.minheap) and -self.maxheap[0] > self.minheap[0]
            ):
                heappush(self.minheap, -heappop(self.maxheap))
            if len(self.maxheap) < len(self.minheap):
                heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-self.maxheap[0])) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

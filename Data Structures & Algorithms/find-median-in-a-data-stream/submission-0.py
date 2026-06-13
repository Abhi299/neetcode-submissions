from heapq import heapify, heappush, heappop

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.right and self.right[0] <= num:
            heappush(self.right, num)
            num = heappop(self.right)
        heappush(self.left, -num)

        # balance
        if len(self.left) > len(self.right) + 1:
            heappush(self.right, -heappop(self.left))

    def findMedian(self) -> float:
        n = len(self.left) + len(self.right)

        if n & 1:
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2
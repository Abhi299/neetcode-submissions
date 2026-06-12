from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums
        heapify(minheap)

        while len(minheap) > k:
            heappop(minheap)

        print(minheap)

        return minheap[0]
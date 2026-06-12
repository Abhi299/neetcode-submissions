from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heapify(maxheap := [(1, -freq, key) for key, freq in Counter(tasks).items()])

        T = 1
        while maxheap:
            wakeupT, freq, taskId = heappop(maxheap)

            if wakeupT > T:
                T = wakeupT
            
            freq += 1
            nwakeupT = wakeupT + n + 1

            if freq != 0:
                heappush(maxheap, (nwakeupT, freq, taskId))

            T += 1

        return T - 1
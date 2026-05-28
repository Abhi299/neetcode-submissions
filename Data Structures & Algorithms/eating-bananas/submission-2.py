class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def is_valid(mid):
            t = 0
            for p in piles:
                t += math.ceil(p / mid)
            return t <= h

        while l < r:
            mid = l + (r - l) // 2

            if is_valid(mid):
                r = mid
            else:
                l = mid + 1
        return r
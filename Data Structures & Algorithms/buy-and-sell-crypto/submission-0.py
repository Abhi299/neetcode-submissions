class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, mx, left_min = len(prices), 0, math.inf

        for i in range(n):
            mx = max(mx, prices[i] - left_min)
            left_min = min(prices[i], left_min)
        return mx
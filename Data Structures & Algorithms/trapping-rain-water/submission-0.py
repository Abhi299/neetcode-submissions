class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, n = [], len(height)
        currMax = 0

        for h in height:
            maxLeft.append(currMax)
            currMax = max(currMax, h)

        maxRight = []
        currMax = 0

        for h in reversed(height):
            maxRight.append(currMax)
            currMax = max(currMax, h)
        maxRight.reverse()

        water = [0] * n

        for i, h in enumerate(height):
            water[i] = max(water[i], min(maxLeft[i], maxRight[i]) - h)
        
        return sum(water)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right, max_contr = [0] * n, [0] * n, [0] * n

        stack = []

        # Closest smaller to left
        for i, h in enumerate(heights):
            while stack and stack[-1][0] >= h:
                stack.pop()

            left[i] = stack[-1][1] if stack else -1

            stack.append((h, i))

        stack = []
        # Closest smaller to right
        for i in range(n - 1, -1, -1):
            h = heights[i]

            while stack and stack[-1][0] >= h:
                stack.pop()

            right[i] = stack[-1][1] if stack else n

            stack.append((h, i))

        for i, h in enumerate(heights):
            l, r = i - left[i], right[i] - i
            w = l + r - 1
            max_contr[i] = h * w

        return max(max_contr, default=0)
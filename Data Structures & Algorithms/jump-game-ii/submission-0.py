class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        jumps = 0
        n = len(nums)

        if n <= 1: return 0

        for i in range(n):
            new_r = r
            for node in range(l, min(n, r + 1)):
                new_r = max(r, node + nums[node])
                if new_r >= n - 1:
                    return jumps + 1
            l = r + 1
            r = new_r
            jumps += 1
        return jumps
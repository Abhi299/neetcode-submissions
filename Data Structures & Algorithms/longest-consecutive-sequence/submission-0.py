class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if num - 1 not in numset:
                l = 0
                while num in numset:
                    l += 1
                    num += 1
                longest = max(l, longest)
        return longest   
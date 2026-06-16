class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        ans = [intervals[0]]

        for i in range(1, n):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans
    
    def partitionLabels(self, s: str) -> List[int]:
        flo = {}

        for i, ch in enumerate(s):
            if ch not in flo:
                flo[ch] = [i, i]
            else:
                flo[ch][1] = i
        
        intervals = list(flo.values())

        res = []

        for s, e in self.merge(intervals):
            res.append(e - s + 1)
        
        return res
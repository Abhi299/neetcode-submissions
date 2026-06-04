class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def valid(r, l, freq):
            return (r - l + 1 == len(freq))
        n = len(s)
        freq = Counter()
        l = 0
        ans = 0
        for r in range(n): # N
            freq[s[r]] += 1 # My window might be invalid
            # Ensure window is valid
            while not valid(r, l, freq):
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            # Now my window is valid
            ans = max(ans, r - l + 1)
        return ans
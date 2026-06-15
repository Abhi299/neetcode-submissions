class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False

        num_groups = n // groupSize
        freq = Counter(hand)

        for i in range(num_groups):
            start = min(freq.keys())
            for _ in range(groupSize):
                if start not in freq: return False

                freq[start] -= 1
                if freq[start] == 0: del freq[start]
                start += 1
        return True
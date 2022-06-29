from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = sorted(Counter(s).values(), reverse=True)
        remove = 0
        freeFreq = len(s)
        for freq in frequencies:
            freeFreq = min(freeFreq, freq)
            remove += freq - freeFreq
            if freeFreq > 0:
                freeFreq -= 1
        return remove

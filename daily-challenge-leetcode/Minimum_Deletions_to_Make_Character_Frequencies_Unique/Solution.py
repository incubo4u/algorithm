from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s) == 1:
            return
        remove = 0
        freq = list(Counter(s).values())
        freq.sort(reverse=True)
        i, j = 0, 1
        while j < len(freq):
            if freq[i] <= 0:
                break
            if freq[i] == freq[j]:
                remove += 1
                freq[j] -= 1
                if j + 1 < len(freq):
                    j += 1
            else:
                i += 1
                j = i + 1
        return remove
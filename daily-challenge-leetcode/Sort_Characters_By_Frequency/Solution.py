from collections import Counter


class Solution:

    def frequencySort(self, s: str) -> str:
        return "".join(
            [c * freq for _, (c, freq) in enumerate(Counter(s).most_common())])

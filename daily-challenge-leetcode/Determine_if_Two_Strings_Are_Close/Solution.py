from typing import Counter


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return tuple(sorted(c1.values())) == tuple(sorted(
            c2.values())) and c1.keys() == c2.keys()

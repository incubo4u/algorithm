from functools import cmp_to_key
from typing import List


class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        def cmp(a, b):
            for i in range(max(len(a), len(b))):
                if i > len(a) - 1:
                    return -1
                elif i > len(b) - 1:
                    return 1
                elif abc[a[i]] > abc[b[i]]:
                    return 1
                elif abc[a[i]] < abc[b[i]]:
                    return -1
            return 0

        abc = {letter: i for i, letter in enumerate(order)}
        tmp = words[::]
        words.sort(key=cmp_to_key(cmp))
        return words == tmp
from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for i, s in enumerate(map(lambda x: list(map(ord, x)), strings)):
            key = ""
            for j in range(len(s)):
                if j == len(s) - 1:
                    key += str((s[j] - s[j - 1]) % 26)
                    break
                key += str((s[j] - s[j + 1]) % 26)
            ret[key].append(strings[i])
        return ret.values()
